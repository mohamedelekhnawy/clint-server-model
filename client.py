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
host="127.0.0.1"
port=65432
s.connect((host, port))
t1=Thread(target=send,args=(s,))
t2=Thread(target=receive,args=(s,))
t1.start()
t2.start()
    

    

        