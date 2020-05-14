# server.py
import socket
import time

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 13
#as in notes; the day-time server must have port no 13
# bind to the port
ss.bind((host, port))
ss.listen(5)
while True:

    cs, addr = ss.accept()
    print("Connected to %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    cs.send(currentTime.encode('ascii'))
    cs.close()