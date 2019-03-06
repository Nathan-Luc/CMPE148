from __future__ import division
import socket
import math
import pickle

#TCP protocol
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#get the IP of the host
ip = socket.gethostbyname(socket.gethostname())
port = 3434
address = (ip,port)

#attempt to bind socket to the address and port
server.bind(address)
print "[=] Socket bind successful"

#listen on socket
server.listen(1)
print "[=] Started listening "

#establish connection with client
client,addr= server.accept()
print "[=] Connection established with Client"

#loop to maintain function
list=[]
while True:

        #Receiving data from the client 
        data = pickle.loads(client.recv(4096))

        #data = pickle.loads(recvd_data)
        print ('User input value: ' , data)
        #convert input into a float
        ##for i in range(data):
         #       list.append(data)
        #print("List values: ", list)
        #square root the number if it is greater than 0
        #if(data >= 0):
             #   x = math.sqrt(data)
          #      x = str(x)
           #     client.send(x)
        #if the number input is a negative number  we send this message to client
       # elif(data < 0):
         #       errormsg = 'Cannot find square root of negative number'
         #       client.send(errormsg)
   
        max_value=max(data)
        ms=pickle.dumps(max_value)
        client.send(ms)
