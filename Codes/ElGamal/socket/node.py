import socket
import sys

from Crypto.PublicKey.pubkey import *
from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util import number

p = number.getPrime(160 , Random.new().read)

g = number.getRandomRange(3, p-1)
p = str(p)
g = str(g)

HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
connection_list = [s]

conn, addr = s.accept()
print('Connected by', addr)
while connection_list:
    data = conn.recv(1024)
    if data:
        if str(data) == 'generate':
            conn.send(p,g)
            
        else:
            conn.send(data)
    else:
        break
conn.close()
