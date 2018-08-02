from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util import number

#(t, n) - (3, 5)

p = number.getPrime(16)
g = number.getRandomRange(1,p-1)
a = number.getRandomRange(1,p-1)
y = pow(g,a)

print (p,g,a,y)
