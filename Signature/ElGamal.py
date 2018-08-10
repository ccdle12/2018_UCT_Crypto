
import time
from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD
from Crypto.Hash import SHA

start_time = time.time()
message = "Hello"
key = ElGamal.generate(160, Random.new().read)
#h = SHA.new(message).digest()

while 1:
     k = random.StrongRandom().randint(1,key.p-1)
     if GCD(k,key.p-1)==1: break

sig = key.sign(message,k)

if key.verify(message,sig):
     print "OK"
else:
     print "Incorrect signature"

print("--- %s seconds ---" %(time.time() - start_time))
