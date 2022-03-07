import socket
import threading
import time

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


# Send the message to Tello and allow for a delay in seconds
def send(message, delay):
    # Try to send the message otherwise print the exception
    try:
        sock1.sendto(message.encode(), tello1_address)
        sock2.sendto(message.encode(), tello2_address)
        print("Sending message: " + message)
    except Exception as e:
        print("Error sending: " + str(e))

    # Delay for a user-defined period of time
    time.sleep(delay)


# Receive the message from Tello
def receive():
    # Continuously loop and listen for incoming messages
    while True:
        # Try to receive the message otherwise print the exception
        try:
            response1, ip_address = sock1.recvfrom(128)
            response2, ip_address = sock2.recvfrom(128)
            print("Received message: from Tello EDU #1: " + response1.decode(encoding='utf-8'))
            print("Received message: from Tello EDU #2: " + response2.decode(encoding='utf-8'))

        except Exception as e:
            # If there's an error close the socket and break out of the loop
            sock1.close()
            sock2.close()

            print("Error receiving: " + str(e))
            break


# Create and start a listening thread that runs in the background
# This utilizes our receive functions and will continuously monitor for incoming messages
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

tile = 75
#nr 1
send("command", 4)
send("battery?", 4)
send("mon", 4)

# Send the takeoff command
send("takeoff", 5)

#1
# Start
#2
# send("up 100", delay)
#3
send("up 150", delay)
#4
send("down 200", delay)
#5
send("back 0", delay)
#6
send("forward 0", delay)
#7
send("up 300", delay)
#8
send("ccw 360", 8)
#9
send("up 250", delay)
#10
send("forward 0", delay)
#11
send("back 0", delay)
#12
send("right 0", delay)
#13
send("right 0", delay)
#14
send("up 0", delay)
#15
send("up 150", delay)
#16
send(f'right {1 * tile }', delay)
#17
send(f'left {2 * tile }', delay)
#18
send("cw 45", delay)
#19
send(f'forward {1.5 * tile }', delay)
#20
send("cw 90", delay)
#21
send(f'forward {1.5 * tile }', delay)
#22
send("cw 90", delay)
#23
send(f'forward {1.5 * tile }', delay)
#24
send("cw 90", delay)
#25
send(f'forward {1.5 * tile }', delay)
#26
send("cw 45", delay)
#27
send(f'right {1 * tile }', delay)
#28
send("forward 0", delay)
#29
send("forward 0", delay)
#30
send("down 100", delay)
#31
send("flip f", delay)
#32
send("down 100", delay)
#33
send("flip f", delay)
#34
send("flip b", delay)
#35
send("land", 5)


# Print message
print("Mission completed successfully!")

# Close the socket
sock1.close()

#nr 2
send("command", 4)
send("battery?", 4)
send("mon", 4)

# Send the takeoff command
send("takeoff", 5)

#1
# Start
#2
# send("up 100", delay)
#3
send(f'forward {1 * tile }', delay)
send(f'left {1 * tile }', delay)
#4
send("up 50", delay)
#5
send(f'back {1 * tile }', delay)
send(f'right {1 * tile }', delay)
#6
send(f'forward {2 * tile }', delay)
#7
send("down 50", delay)
#8
send("ccw 360", 8)
#9
#10
send(f'forward {1 * tile }', delay)
#11
send(f'back {1 * tile }', delay)
#12
send(f'right {1 * tile }', delay)
#13
send(f'right {0 * tile }', delay)
#14
send("up 100", delay)
#15
send("down 50", delay)
#16
send(f'right {2 * tile }', delay)
#17
send(f'left {4 * tile }', delay)
#18
send(f'forward {2 * tile }', delay)
#19
send(f'forward {1 * tile }', delay)
#20
send(f'right {1 * tile }', delay)
#21
send(f'right {2 * tile }', delay)
#22
send(f'right {1 * tile }', delay)
#23
send(f'back {1 * tile }', delay)
#24
send(f'back {2 * tile }', delay)
#25
send(f'back {1 * tile }', delay)
#26
send(f'left {1 * tile }', delay)
#27
send(f'left {2 * tile }', delay)
#28
send(f'forward {1 * tile }', delay)
#29
send(f'forward {2 * tile }', delay)
#30
send("down 100", delay)
#31
send("flip f", delay)
#32
send("up 300", delay)
#33
send("flip f", delay)
#34
send("flip b", delay)
#35
send("land", 5)

# Print message
print("Mission completed successfully!")

# Close the socket
sock1.close()


#nr 3 drone 62
send("command", delay)
send("battery?", delay)
send("mon", delay)

# Send the takeoff command
send("takeoff", delay)

#1
# Start
#2
# send("up 100", delay)
#3
send(f'forward {1 * tile }', delay)
send(f'right {1 * tile }', delay)
#4
send("up 50", delay)
#5
send(f'back {1 * tile }', delay)
send(f'left {1 * tile }', delay)
#6
send(f'forward {2 * tile }', delay)
#7
send("down 50", delay)
#8
send("cw 360", 8)
#9
send(f'left {0 * tile }', delay)
#10
send(f'forward {1 * tile }', delay)
#11
send(f'forward {1 * tile }', delay)
#12
send(f'left {1 * tile }', delay)
#13
send(f'left {0 * tile }', delay)
#14
send("up 100", delay)
#15
send("down 50", delay)
#16
send(f'right {2 * tile }', delay)
#17
send(f'left {4 * tile }', delay)
#18
send(f'forward {1 * tile }', delay)
#19
send(f'right {1 * tile }', delay)
#20
send(f'right {2 * tile }', delay)
#21
send(f'right {1 * tile }', delay)
#22
send(f'back {1 * tile }', delay)
#23
send(f'back {2 * tile }', delay)
#24
send(f'back {1 * tile }', delay)
#25
send(f'left {1 * tile }', delay)
#26
send(f'left {2 * tile }', delay)
#27
send(f'forward {1 * tile }', delay)
#28
send(f'forward {2 * tile }', delay)
#29
send(f'right {2 * tile }', delay)
#30
send("down 100", delay)
#31
send("flip f", delay)
#32
send("up 300", delay)
#33
send("flip f", delay)
#34
send("flip b", delay)
#35
send("land", 5)

# send("flip f", delay)
# send("flip b", delay)

# Print message
print("Mission completed successfully!")

# Close the socket
sock1.close()

# nr 4
send("command", 4)
send("battery?", 4)
send("mon", 4)

# Send the takeoff command
send("takeoff", 5)

#1
# Start
#2
# send("up 100", delay)
#3
send(f'back {1 * tile }', delay)
send(f'left {1 * tile }', delay)
#4
send("up 50", delay)
#5
send(f'forward {2 * tile }', delay)
#6
send(f'forward {1 * tile }', delay)
send(f'right {1 * tile }', delay)
#7
send("down 50", delay)
#8
send("ccw 360", 8)
#9
send(f'left {0 * tile }', delay)
#10
send(f'left {1 * tile }', delay)
send(f'back {1 * tile }', delay)
#11
send(f'forward {2 * tile }', delay)
#12
send(f'right {2 * tile }', delay)
#13
send("up 50", delay)
#14
send("down 50", delay)
#15
send(f'left {0 * tile }', delay)
#16
send(f'right {2 * tile }', delay)
#17
send(f'left {4 * tile }', delay)
#18
send(f'right {1 * tile }', delay)
#19
send(f'right {2 * tile }', delay)
#20
send(f'right {1 * tile }', delay)
#21
send(f'back {1 * tile }', delay)
#22
send(f'back {2 * tile }', delay)
#23
send(f'back {1 * tile }', delay)
#24
send(f'left {1 * tile }', delay)
#25
send(f'left {2 * tile }', delay)
#26
send(f'forward {1 * tile }', delay)
#27
send(f'forward {2 * tile }', delay)
#28
send(f'right {2 * tile }', delay)
#29
send(f'back {2 * tile }', delay)
#30
send("up 100", delay)
#31
send("flip b", delay)
#32
send("up 150", delay)
#33
send("flip f", delay)
#34
send("flip b", delay)
#35
send("land", 5)


# Print message
print("Mission completed successfully!")

# Close the socket
sock1.close()


#nr 5
send("command", 4)
send("battery?", 4)
send("mon", 4)

# Send the takeoff command
send("takeoff", 5)

#1
# Start
#2
# send("up 100", delay)
#3
send(f'back {1 * tile }', delay)
send(f'right {1 * tile }', delay)
#4
send("up 50", delay)
#5
send(f'forward {2 * tile }', delay)
#6
send(f'forward {1 * tile }', delay)
send(f'left {1 * tile }', delay)
#7
send("down 50", delay)
#8
send("cw 360", 8)
#9
send(f'left {0 * tile }', delay)
#10
send(f'right {1 * tile }', delay)
send(f'back {1 * tile }', delay)
#11
send(f'back {2 * tile }', delay)
#12
send(f'left {2 * tile }', delay)
#13
send("up 50", delay)
#14
send("down 50", delay)
#15
send(f'left {0 * tile }', delay)
#16
send(f'right {2 * tile }', delay)
#17
send(f'left {4 * tile }', delay)
#18
send(f'forward {1 * tile }', delay)
#19
send(f'forward {2 * tile }', delay)
#20
send(f'forward {1 * tile }', delay)
#21
send(f'right {1 * tile }', delay)
#22
send(f'right {2 * tile }', delay)
#23
send(f'right {1 * tile }', delay)
#24
send(f'back {1 * tile }', delay)
#25
send(f'back {2 * tile }', delay)
#26
send(f'back {1 * tile }', delay)
#27
send(f'left {1 * tile }', delay)
#28
send(f'left {2 * tile }', delay)
#29
send(f'forward {1 * tile }', delay)
#30
send("up 100", delay)
#31
send("flip b", delay)
#32
send("up 150", delay)
#33
send("flip f", delay)
#34
send("flip b", delay)
#35
send("land", 5)

# Print message
print("Mission completed successfully!")

# Close the socket
sock1.close()



