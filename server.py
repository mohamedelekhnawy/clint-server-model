from socket import *
from threading import Thread


def send(s):
    while True:
        msg=input("Send...")
        s.send(bytes(msg,"utf-8"))

def receive(s):
    while True:
        msg =s.recv(1024)
        print(msg.decode("utf-8"))        

s=socket(AF_INET, SOCK_STREAM)
host ="127.0.0.1"
port = 65432
s.bind((host, port))
s.listen(5)

while True:
    con,addr=s.accept()
    print("got conn from :" ,addr)

    t1=Thread(target=send,args=(con,))
    t2=Thread(target=receive,args=(con,))
    t1.start()
    t2.start()
    




