import socket

def start_intermediary(port):
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
                
def forward_command(command):
    target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target_socket.connect(('localhost', 65434))
    target_socket.sendall(command.encode())
    target_socket.close()

if __name__ == "__main__":
    start_intermediary(65433)