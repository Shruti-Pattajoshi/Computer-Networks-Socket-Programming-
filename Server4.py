# server.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 7878

s.bind((host, port))

while True:

    req, addr1 = s.recvfrom(1024)
    print("Got a connection from : %s" % str(addr1))
    print("Query Received from Client : %s" % req.decode())
    ans = req.decode()
    f = open("directory.txt", "r")
    fl = f.readlines()

    for x in fl:

        text = x.split(";")
        if text[1] == ans:
            message = text[0]
            s.sendto(message.encode(), addr1)
            print("Query Answer sent!!")
        if text[0] == ans:
            message = text[1]
            s.sendto(message.encode(), addr1)
            print("Query Answer sent!!")

        continue

    s.close()
    break