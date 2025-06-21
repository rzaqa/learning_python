import socket
import sys


HOST = '127.0.0.1'
PORT = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f'[*] Listening on {HOST}:{PORT}')

while True:
    try:
        client_socket, address = server_socket.accept()
    except KeyboardInterrupt:
        print("\nClosing Server Socket...")
        server_socket.close()
        sys.exit()

    print(f'[*] Accepted connection from {address[0]}:{address[1]}')
    request = client_socket.recv(1024)
    print(f'[*] Received: {request.decode("utf-8")}')
    client_socket.send(b'THIS IS SERVER SPEAKING')
    client_socket.close()







# def main():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind((HOST, PORT))
#     server_socket.listen(5)
#     print(f'[*] Listening on {HOST}:{PORT}', " Press Ctrl-C to Exit")
#
#     while True:
#         try:
#             client, address = server_socket.accept()
#         except KeyboardInterrupt:
#             print("\nClosing Server Socket...")
#             server_socket.close()
#             sys.exit()
#
#         print(f'[*] Accepted connection from {address[0]}:{address[1]}')
#         client_handler = threading.Thread(target=handle_client, args=(client,))
#         client_handler.start()
#
#
# def handle_client(client_socket):
#     with client_socket as sock:
#         request = sock.recv(1024)
#         print(f'[*] Received: {request.decode("utf-8")}')
#         sock.send(b'THIS_IS_THE_SERVER_SPEAKING')
#
#
# if __name__ == '__main__':
#     main()
