import webbrowser
import random
import socket

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


urls = [
    ("https://www.rizz.com", 1),
    ("https://www.youtube.com", 2),
    ("https://www.time.gov", 3),
    ("https://www.X.com",4),
    ("https://www.reddit.com",5),
    ("https://www.google.com",6),
    ("http://weavesilk.com",7),
    ("https://docs.google.com/presentation/d/1xfiSekexO7YSV1lYd2g6-tUJ1Q7MBdjldGstJW1Yfpc/edit#slide=id.g1f50854902b_0_0",8),
    ("https://store.steampowered.com",9),
    ("https://clicktheredbutton.com",10),
    ("https://www.youtube.com/watch?v=EkHoJqJwDkY",11),
    ("https://clicktheredbutton.com",12),
    ("https://www.youtube.com/watch?v=6QtuIymUzRU&t=1404s",13),
    ("https://www.youtube.com/watch?v=2lI9_lAXG_k",14),
    ("https://fart.com",15),
]

# Register the browser
webbrowser.register('opera', None, webbrowser.BackgroundBrowser("C:\\Users\\David\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"))
print("Browser registered successfully.")


browser = webbrowser.get('opera')
if browser is not None:
    print("Using Opera GX browser.")
else:
    print("Failed to get Opera GX browser.")

def execute_command(command):
    if command == "youtube":
        webbrowser.open(urls[1][0])  
    elif command == "steam":
        webbrowser.open(urls[8][0])  
    elif command == "reddit":
        webbrowser.open(urls[4][0]) 
    elif command == "random video":
        # Select a random video 
        webbrowser.open(random.choice([urls[10][0], urls[11][0], urls[12][0]]))
    elif command == "weavesilk" or command == "weave silk":
        webbrowser.open(urls[6][0]) 
    elif command == "x":
        webbrowser.open(urls[3][0])
    elif command == "time":
        webbrowser.open(urls[2][0])
    elif command == "google":
        webbrowser.open(urls[5][0])
    elif command == "google docs":
        webbrowser.open(urls[7][0])
    elif command == "rizz" or "riz":
        webbrowser.open(urls[0][0])
    elif command == "fart":
        webbrowser.open(urls[14][0])
    else:
        webbrowser.open("https://" + command + ".com")


if __name__ == "__main__":
    start_server(65434)
