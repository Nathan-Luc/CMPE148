import socket
import pickle
client = socket.socket()

#TCP procotol
ip = socket.gethostbyname(socket.gethostname())
client.connect((ip,3434))
list1=[]

while True:
    
    number = int(input("Enter list length "))
    for i in range(number):
        data = (int(input()))
        list1.append(data)

    sdata=pickle.dumps(list1)
    client.send(sdata)
    print 'You entered the value: ' , list1
    
    max_value = pickle.loads(client.recv(4096))
    print 'Max value: ', max_value

    min_value = pickle.loads(client.recv(4096))
    print 'Min value: ' , min_value
   
    sum_value = pickle.loads(client.recv(4096))
    print 'Sum value: ', sum_value

    avg_value = client.recv(4096)
    print 'Avg value: ', avg_value
    break;
client.close()
  
