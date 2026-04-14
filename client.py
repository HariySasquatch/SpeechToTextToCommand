import speech_recognition as sr
import pyttsx3 
import pyautogui as mouse
import socket
import tkinter as tk

def cursor_up():
    x, y = mouse.position()  
    mouse.moveTo(x, y - 100)
    return "Moved up."

def cursor_down():
    x, y = mouse.position()  
    mouse.moveTo(x, y + 100)
    return "Moved down."

def cursor_left():
    x, y = mouse.position() 
    mouse.moveTo(x - 100, y)
    return "Moved left."

def cursor_right():
    x, y = mouse.position()  
    mouse.moveTo(x + 100, y)
    return "Moved right."

def cursor_left_click():
    mouse.leftClick()
    return "Left clicked."

def cursor_right_click():
    mouse.rightClick()
    return "Right clicked."

def dev_mode():
    print("Entering Dev Mode. Type 'exit' to leave Dev Mode.")
    while True:
        command3 = input("Dev> ")  # Take user input from the console
        if command3.lower() == "exit":
            print("Exiting Dev Mode.")
            break
        try:
            result = exec(command3, globals())
            if result is not None:
                print(result)
        except Exception as e:
            print(f"Error: {e}")

def send_command(thing):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65433))
    client_socket.sendall(thing.encode())
    client_socket.close()

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)

    print(f"Server is listening on port {port}")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)
            if data:
                command = data.decode()
                print("Received command:", command)


r = sr.Recognizer()

def SpeakText(command2):
    
    engine = pyttsx3.init()
    engine.say(command2) 
    engine.runAndWait()

def speech():
    global MyText
   
    try:
        # Use the microphone as source for input.
        print("Please talk into the mic to use the speech to text.")
        with sr.Microphone() as source2:
           
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            print("listening...")
            audio2 = r.listen(source2)
            
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            
            print("STT heard: " + MyText)
            SpeakText(MyText)
            return MyText  # Return the recognized text
    
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
    except sr.UnknownValueError:
        print("Unknown error occurred")

def open_website(website_name):
    if website_name in sites:
        send_command(website_name)

sites = ("random video", "youtube", "steam", "reddit", "random video", "weavesilk" or "weave silk", "x", "time", "google", "fart", "google docs")

def handle_sites():
    while True:
        MyText = speech() 
        if MyText is not None:
            if any(website in MyText for website in sites):  # Check if any website is mentioned
                for website in sites:
                    if website in MyText:
                        open_website(website)
                        return  

# Main loop
while True:
    MyText = speech()

    if MyText is not None:  # Check if speech input is recognized
        MyText = MyText.lower() 

        if "mouse down" in MyText or "down" in MyText:
            x, y = mouse.position()
            mouse.moveTo(x, y + 100)

        if "mouse up" in MyText or "up" in MyText:
            x, y = mouse.position()  
            mouse.moveTo(x, y - 100)

        if "mouse left" in MyText or "left" in MyText:
            x, y = mouse.position()  
            mouse.moveTo(x - 100, y)

        if "mouse right" in MyText or "right" in MyText:
            x, y = mouse.position()  
            mouse.moveTo(x + 100, y)

        if "left click" in MyText:
            mouse.leftClick()

        if "right click" in MyText:
            mouse.rightClick()

        if "web" in MyText or "browser" in MyText:
            handle_sites()  # Handle the pause for recognizing website commands

        if "dev mode" in MyText or "dev" in MyText:
            print("You sure do want it...")
            dev_mode()  # Enter Dev mode when "dev mode" is recognized

            break

    else:
        print("Not a command.")
    
