# client.py
import socket

sp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 13
sp.connect((host, port))
msg = sp.recv(1024)
sp.close()

print("The time recieved from the server is: %s" % msg.decode('ascii'))