from __future__ import division
import socket
import math
import pickle
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
        data,addr = server.recvfrom(4096)
        load = pickle.loads(data)
        print 'User input value: ' , load
        print 'Data recieved fron ' , addr
   
        max_value=max(load)
        max_send=pickle.dumps(max_value)
        print 'Max: ', max_value
        server.sendto(max_send,addr)

        min_value= min(load)
        min_send = pickle.dumps(min_value)
        print 'Min: ', min_value
        server.sendto(min_send, addr)

        sum_value= sum(load)
        sum_send = pickle.dumps(sum_value)
        print 'Sum: ', sum_value
        server.sendto(sum_send, addr)


        avg_value = sum(load)/len(load)
        avg_send = str(avg_value)
        print 'Avg value :', float(avg_value)
        server.sendto(avg_send,addr)
        break

server.close()
print 'Connection Closed'
