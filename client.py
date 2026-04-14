import speech_recognition as sr
import pyttsx3 
import pyautogui as mouse
import socket
import tkinter as tk
import sys

def cursor_up():
    x, y = mouse.position()  # Correct use of mouse.position()
    mouse.moveTo(x, y - 100)
    return "Moved up."

def cursor_down():
    x, y = mouse.position()  # Correct use of mouse.position()
    mouse.moveTo(x, y + 100)
    return "Moved down."

def cursor_left():
    x, y = mouse.position()  # Correct use of mouse.position()
    mouse.moveTo(x - 100, y)
    return "Moved left."

def cursor_right():
    x, y = mouse.position()  # Correct use of mouse.position()
    mouse.moveTo(x + 100, y)
    return "Moved right."

def cursor_left_click():
    mouse.leftClick()
    return "Left clicked."

def cursor_right_click():
    mouse.rightClick()
    return "Right clicked."

def play_audio():
    send_command("audio")
    return "Playing audio."

def stop_audio():
    send_command("stop audio")
    return "Stopped audio."

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




# Initialize speech recognition
r = sr.Recognizer()

def SpeakText(command2):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command2) 
    engine.runAndWait()

def speech():
    global MyText
    # Exception handling to handle exceptions at the runtime
    try:
        # Use the microphone as source for input.
        print("Please talk into the mic to use the speech to text thingy.")
        with sr.Microphone() as source2:
            # Wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            # Listen for the user's input 
            print("listening...")
            audio2 = r.listen(source2)
            
            # Using Google to recognize audio
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

def handle_pause():
    while True:
        MyText = speech()  # Get speech input
        if MyText is not None:
            if any(website in MyText for website in sites):  # Check if any website is mentioned
                for website in sites:
                    if website in MyText:
                        open_website(website)
                        return  # Exit the pause loop once a website is opened

# Main loop
while True:
    MyText = speech()

    if MyText is not None:  # Check if speech input is recognized
        MyText = MyText.lower()  # Convert the recognized text to lowercase

        if "mouse down" in MyText or "down" in MyText:
            x, y = mouse.position()  # Correct use of mouse.position()
            mouse.moveTo(x, y + 100)

        if "mouse up" in MyText or "up" in MyText:
            x, y = mouse.position()  # Correct use of mouse.position()
            mouse.moveTo(x, y - 100)

        if "mouse left" in MyText or "left" in MyText:
            x, y = mouse.position()  # Correct use of mouse.position()
            mouse.moveTo(x - 100, y)

        if "mouse right" in MyText or "right" in MyText:
            x, y = mouse.position()  # Correct use of mouse.position()
            mouse.moveTo(x + 100, y)

        if "left click" in MyText:
            mouse.leftClick()

        if "right click" in MyText:
            mouse.rightClick()

        if "web" in MyText or "browser" in MyText:
            handle_pause()  # Handle the pause for recognizing website commands

        if "i like balls" in MyText or "balls" in MyText:
            print("You sure do like it...")
            dev_mode()  # Enter Dev mode when "dev mode" is recognized

            break
        if "random audio" in MyText or "audio" in MyText:
            send_command("audio")

        if "stop audio" in MyText or "end audio" in MyText or "stop random audio" in MyText:
            send_command("stop audio")

    else:
        print("Not a command.")
    
