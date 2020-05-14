# client.py
import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()
port = 8888

server_addr_port = (host, port)

while True:

    print("Enter message to send to the server:")
    message = input(" >> ")
    client_sock.sendto(message.encode(),server_addr_port)
    msg, adr = client_sock.recvfrom(1024)
    print("Message Received from the server : %s" % msg.decode())
    client_sock.close()
    break
