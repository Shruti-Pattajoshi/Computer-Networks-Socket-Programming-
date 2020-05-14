# client.py
import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 7878
server_addr_port = (host, port)

print("Enter your choice: 1. Search by Name 2. Search by Phone No.")
choice = input()
print("Enter Name or Phone No.")
val = input()

if choice == 2:
    msg = val
else:
    msg = val

client_sock.sendto(msg.encode(), server_addr_port)
buffer_size = 1024
print("Query Sent !!")
mg, addr1 = client_sock.recvfrom(buffer_size)
print("Query Answer received from Server : %s" % mg.decode())
client_sock.close()

