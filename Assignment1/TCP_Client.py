import socket
import pickle
client = socket.socket()

#TCP procotol
ip = socket.gethostbyname(socket.gethostname())
client.connect((ip,3434))
list1=[]

while True:
    
    number = int(input("Enter list length"))
    for i in range(number):
        data = (int(input()))
        list1.append(data)

    sdata=pickle.dumps(list1)
    client.send(sdata)
    print ('You entered the value: ' , list1)
    
    #sqt = client.recv(1024)
    #print "Square root of input is ... " + sqt
    max_value = pickle.loads(client.recv(1024))
    print ('Max value: ', max_value)
