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

while True:


        data = pickle.loads(client.recv(4096))
        print 'User input value: ' , data

   
        max_value=max(data)
        max_send=pickle.dumps(max_value)
        print 'Max: ', max_value
        client.send(max_send)

        min_value= min(data)
        min_send = pickle.dumps(min_value)
        print 'Min: ', min_value
        client.send(min_send)

        sum_value= sum(data)
        sum_send = pickle.dumps(sum_value)
        print 'Sum: ', sum_value
        client.send(sum_send)


        avg_value = sum(data)/len(data)
        avg_send = str(avg_value)
        print 'Avg value :', float(avg_value)
        client.send(avg_send)
        break

client.close()
print 'Connection Closed'
