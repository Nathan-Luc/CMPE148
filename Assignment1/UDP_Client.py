import socket
#UDP protocol
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#example address
address = (socket.gethostbyname(socket.gethostname()),3434)

while True:
    message = raw_input()
    #send the input message to said address
    client.sendto(message, address)
    print 'You entered the value: ' + message

    #receive data from server and save into the variables
    sqt, addr = client.recvfrom(1024)
    print "Square root of input ..." + sqt

    
