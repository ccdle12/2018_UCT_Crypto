import socket
import sys

HOST = '127.0.0.1'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    message = raw_input('input : ')
    s.send((message))
    data = s.recv(1024)
    print('Received',repr(data))

s.close()
