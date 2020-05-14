# server.py
import socket

#udp this time
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()
port = 8888
s.bind((host, port))

while True:

    msg, adr = s.recvfrom(1024)
    print("Got connected to : %s" % str(adr))
    print("Message Received from the client : %s" % msg.decode())
    print("Enter message to send to the client :")
    message = input(" >> ")
    s.sendto(message.encode(), adr)
    s.close()
    break