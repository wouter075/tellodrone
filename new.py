import socket
import threading
import time


drones = [
    '192.168.1.11',
    '192.168.1.12'
]


for x in range(len(drones)):
    # Create a UDP connection that we'll send the command to
    print(x)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

exit()
delay = 7

# IP and port of Tello

tello1_address = ('192.168.1.11', 8889)
tello2_address = ('192.168.1.12', 8889)

# IP and port of local computer
local1_address = ('', 9010)
local2_address = ('', 9011)

# Create a UDP connection that we'll send the command to
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the local address and port
sock1.bind(local1_address)
sock2.bind(local2_address)


def send(message, delay, sock, drone):
    # Try to send the message otherwise print the exception
    try:
        sock.sendto(message.encode(), drone)
        print("Sending message: " + message)
    except Exception as e:
        print("Error sending: " + str(e))

    # Delay for a user-defined period of time
    time.sleep(delay)


def receive(sock):
    # Continuously loop and listen for incoming messages
    while True:
        # Try to receive the message otherwise print the exception
        try:
            response1, ip_address = sock.recvfrom(128)
            # response2, ip_address = sock2.recvfrom(128)
            print("Received message: from Tello EDU #1: " + response1.decode(encoding='utf-8'))
            # print("Received message: from Tello EDU #2: " + response2.decode(encoding='utf-8'))

        except Exception as e:
            # If there's an error close the socket and break out of the loop
            sock.close()
            print("Error receiving: " + str(e))
            break


receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()
