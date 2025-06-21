import socket

HOST = "127.0.0.1"
PORT = 10000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    client_socket.connect((HOST, PORT))
    message = b"THIS IS THE CLIENT SPEAKING"
    print("Sending :", message.decode("utf-8"))
    client_socket.send(message)
    response = client_socket.recv(4096)
    print("Received :", response.decode('utf-8'))
    client_socket.close()
