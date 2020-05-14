import socket
import select
import errno

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234
my_username = input("Enter your IP Address : ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
self_ip = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:
    #Sender Client sends a ping request - sending its MAC addr and the reciever IP addr splitted by ';'

    print('Give your MAC Address;IP_Destination : (__;__)')
    message = input(f'{my_username} > ')

    if message:

        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)
        print('Sending Ping Request')
        print('Ping packet sent to the server!')

#initially i made only one client program and kept the above n the below part in a if-else statement. but now
#since i was to debug, i made one recieving client (Client_ARP_2) and one sender one(Client_ARP) hence commenting below part

"""    # Wait for user to input a message
    try:
    # Now we want to loop over received messages (there might be more than one) and print them
            while True:

                # Receive our "header" containing username length, it's size is defined and constant
                username_header = client_socket.recv(HEADER_LENGTH)

                # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
                if not len(username_header):
                    print('Connection closed by the server')
                    sys.exit()

                # Convert header to int value
                username_length = int(username_header.decode('utf-8').strip())
                print('Hey i m starting reading of your message!!')
                # Receive and decode username
                username = client_socket.recv(username_length).decode('utf-8')

                print('Hey i m reading your message!!')
                # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
                message_header = client_socket.recv(HEADER_LENGTH)
                message_length = int(message_header.decode('utf-8').strip())
                message = client_socket.recv(message_length).decode('utf-8')

                print(message)

                if message == self_ip:
                    MAC_Address = "12:34:45:56"
                    message_sending = MAC_Address.encode('utf-8')
                    client_socket.send(message_sending)
                    print('ARP Reply sent : with the MAC Address')
                #check whether the message you have recived actually your IP address or not??
                # Print message

                #if yes then send your mac address back to the server"""

