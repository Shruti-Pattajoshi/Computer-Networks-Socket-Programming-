# client.py
import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
client_sock.connect((host, port))

while True:

    print("Enter message to send to the Server:")
    message = input(" >> ")
    client_sock.send(message.encode())
    client_sock.close()
    break
