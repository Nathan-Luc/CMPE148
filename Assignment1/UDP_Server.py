import socket
import math
#UDP protocol
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#retrieve IP of host
ip = socket.gethostbyname(socket.gethostname())
port = 3434
address = (ip,port)

#attempt to bind socket to the address and port
server.bind(address)
print '[=] Socket bind successful'


#loop to maintain function
while True:

    #Receiving data from the client & address of client
    data,addr = server.recvfrom(1024)
    data = float(data)

    #print on the serverside that the data has been received from such address 
    print 'Data received from', addr 

    #square root the number if it is less than such
    if(data >= 0):
        x = math.sqrt(data)
        x = str(x)
        server.sendto(x, addr)

    #if the number input is negative number we send this message to the client
    elif(data < 0):
        errormsg = 'Cannot find square root of negative number'
        server.sendto(errormsg, addr)
