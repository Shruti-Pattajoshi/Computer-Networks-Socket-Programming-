import socket
import select

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()
sockets_list = [server_socket]
clients = {}
IP_MAC = {}

print(f'Server open for connections on IP - {IP} : Port - {PORT}...')

# Handles message receiving
def receive_message(client_socket):

    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        message_length = int(message_header.decode('utf-8').strip())
        return {'header': message_header, 'data': client_socket.recv(message_length)}
    except:
        return False

while True:

    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    for notified_socket in read_sockets:

        # If new connection from client, accept it
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            # Client should send his IP Address right away, receive it
            user = receive_message(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = user
            IP_MAC[user['data'].decode('utf-8')] = "NA"
            print('Accepted new connection from {}:{}, IP Address: {}'.format(*client_address, user['data'].decode('utf-8')))
           #accepted the connection; got the client's IP Address and put it in the map - mpped with NA as of now

        # Else already connected socket is sending a message - either a arp reply or to send a packet from one client to another
        else:

            # Receive message
            message = receive_message(notified_socket)

            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))

                sockets_list.remove(notified_socket)

                del clients[notified_socket]

                continue


            user = clients[notified_socket]
            # ---> here we got to know its IP address

            # check whether thats a request to ping a packet to another client or it is a arp reply using the ip in the ARP Table
            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            #Now how to differentiate wheather its a packet to be fwded(MAC;IP_destination) or an arp reply (MAC)
            IP_Sender = user["data"].decode("utf-8")
            Message_Recv = message["data"].decode("utf-8")
            message_split = Message_Recv.split(';')
            print(message_split[0])
            print(message_split[1])
            if message_split[1] != 0 :
                print('Its a ping request!')
                IP_Destination = message_split[1]
                MAC_Sender = message_split[0]
                IP_MAC[IP_Sender] = MAC_Sender
                if IP_MAC[IP_Destination] == "NA":

                    print('Sending ARP Request to all other clients!')
                    # Iterate over connected clients and broadcast message
                    for client_socket in clients:

                        # But don't sent it to sender
                        if client_socket != notified_socket:

                            # sent ARP request to find the MAC of the given IP
                            message_sending = message_split[1].encode('utf-8')
                            client_socket.send(message_sending)

                else:
                    print('ARP Table already had the MAC Address so no ARP Request!!')

            else:
                print('ARP Reply recieved!')
                MAC_Destination = message_split[0]
                IP_Destination = user["data"].decode("utf-8")
                IP_MAC[IP_Destination]=MAC_Destination
                print('ARP Table Updated')


 #not necessary to have
    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]