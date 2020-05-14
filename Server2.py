# server.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
# bind to the port
s.bind((host, port))
s.listen(5)
ssock, addr = s.accept()
print("Got a connection from : %s" % str(addr))
while True:

    msg = ssock.recv(1024)
    print("Message Received from Client : %s" % msg.decode())
    ssock.close()
    break