import socket
import select
import errno

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234
my_username = input("Enter your IP Address : ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(1)

username = my_username.encode('utf-8')
self_ip = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:

    '''print('Give your MAC Address;IP_Destination : (__;__)')
    message = input(f'{my_username} > ')
    # If message is not empty - send it

    if message:
        # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)
        print('MAC Address and Destination IP of the packet sent!')'''

    # initially i made only one client program and kept the above n the below part in a if-else statement. but now
    # since i was to debug, i made one recieving client (Client_ARP_2) and one sender one(Client_ARP) hence commented above part

    # Wait for user to input a message
    #try: (removed while debugging)

    #Looping over received messages (ARP requests)

    while True:

        username_header = client_socket.recv(HEADER_LENGTH)

        if not len(username_header):
            print('Connection closed by the server')
            sys.exit()

        #print(username_header.decode('utf-8'))
        #username_length = len(username_header.decode('utf-8'))
        #print(username_length)
        #username_length = int(username_header.decode('utf-8').strip())
        #print('Reached point 1 :Debugging Statement')
                # Receive and decode username
        #username = client_socket.recv(username_length).decode('utf-8')

        print('Reached point 2 :Debugging Statement')

        #the code halts here, I tried removing set block ; after going through some similar errors online
        #but it wasnt helpful; not repeated entries from other client it prints the below things
        #I am unable to find the reason for the same

        message_header = client_socket.recv(HEADER_LENGTH)
        print(message_header)
        message_length = len(message_header.decode('utf-8').strip())
        print(message_length)
        message = client_socket.recv(message_length).decode('utf-8')
        print(message)
        #client_socket.setblocking(0)

        print('Reached point 3 :Debugging Statement')

        if message == username:
            print('Went in : Same IP address :Debugging Statement')
            MAC_Address = "12:34:45:56"
            message_sending = MAC_Address.encode('utf-8')
            client_socket.send(message_sending)
            print('ARP Reply sent : with the MAC Address')
                #check whether the message you have recived actually your IP address or not??
                #if yes then send your mac address back to the server

    #removed for debugging as then only the error will be displayed if any
    '''except IOError as e:
        # This is normal on non blocking connections - when there are no incoming data error is going to be raised
        # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
        # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
        # If we got different error code - something happened
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error 1: {}'.format(str(e)))
            exit()

        # We just did not receive anything
        continue

    except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error 2: '.format(str(e)))
        exit()'''