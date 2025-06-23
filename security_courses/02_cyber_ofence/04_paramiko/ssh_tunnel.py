import getpass
import socket
import select
import sys
import paramiko

def handler(chan, host, port):
    print("Getting a new socket")
    sock = socket.socket()
    try:
        sock.connect((host, port))
    except Exception as e:
        print(f"Forwarding request to {host}:{port} failed with an error: {e}")
        return

    print(f"Connected! Tunnel open {chan.origin_addr} -> {chan.getpeername()} -> {host:port} ")

    while True:
        r,w,x = select.select([sock, chan], [], [])
        if sock in r:
            data = sock.recv(1024)
            if len(data) == 0:
                break
            chan.send(data)
        if chan in r:
            data = chan.recv(1024)
            if len(data) == 0:
                break
            sock.send(data)
    chan.close()
    sock.close()
    print(f"Tunnel closed from {chan.origin_addr}")

def reverse_forward_tunnel(server_port, remote_host, remote_port, transport):
    transport.requset_port_forward("", server_port)
    while True:
        chan = transport.accept(1000)
        print("Opening a New Channel...")
        if chan is None:
            continue # Why?
        handler(chan, remote_host, remote_port)

def main():
    lip = input("Enter SSH Server IP: ")

    lport = input("Enter SSH Server port or <CR>: ") or 22
    lport = int(lport)

    user = input("SSH Server Username: ")
    password = getpass.getpass()

    fport = input("Enter SSH Server Forwarding port or <CR>: ") or 3000
    fport = int(fport)

    rip = input("Enter Remote Server IP: ")
    rport = input("Enter Remote port or <CR>: ")
    rport = int(rport)

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print("Connecting to ssh host {lip}:{lport}")

    try:
        client.connect(lip, lport, user, password)
    except Exception as e:
        print(f"*** Failed to connect to {lip}:{lport} : {e}")
        sys.exit(1)

    print("Now forwarding SSH Server port {fport} to {rip}:{rport}")



if __name__ == "__main__":
    main()

