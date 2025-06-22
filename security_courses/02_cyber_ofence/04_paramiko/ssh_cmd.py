import paramiko
import getpass
import sys

from aiofiles import stderr


def ssh_command(ip, user, passwd, cmd, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    try:
        client.connect(ip, port, user, passwd)
    except Exception as e:
        print(f"Exception: {e}")
        sys.exit()

    try:
        stdin, stdout, stderr = client.exec_command(cmd)
        stdout.channel.recv_exit_status() # EOF?
        output = stdout.read().decode()
        print(f"Returned output:\n {output}")
    except Exception as e:
        print(f"Exception: {e}")
        client.close()
        sys.exit()

    client.close()

if __name__ == "__main__":
    ip = input("Enter server IP: ") or "192.168.1.111"
    port = input("Enter port of <CR>: ") or "22"

    user = input("Username: ")
    password = getpass.getpass()

    cmd = input("Enter command or <CR>: ") or "id"
    ssh_command(ip, user, password, cmd, port)
