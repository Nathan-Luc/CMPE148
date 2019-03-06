import socket
import pickle

#UDP protocol
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#example address
address = (socket.gethostbyname(socket.gethostname()),3434)
list1=[]
while True:
    number = int(input("Enter list length "))
    for i in range(number):
        data = (int(input()))
        list1.append(data)

    sdata=pickle.dumps(list1)
    client.sendto(sdata, address)
    print 'You entered the value: ' , list1

    mv_load,addr= client.recvfrom(4096)
    max_value = pickle.loads(mv_load)
    print 'Max value: ', max_value
    minv_load,addr =client.recvfrom(4096)
    min_value = pickle.loads(minv_load)
    print 'Min value: ' , min_value
    sv_load,addr = client.recvfrom(4096)
    sum_value = pickle.loads(sv_load)
    print 'Sum value: ', sum_value
    avg_value,addr = client.recvfrom(4096)
    print 'Avg value: ', avg_value
    print 'Address Recieved: ', addr
    break
client.close()
print 'Connection Closed'
