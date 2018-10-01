import time
from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA

start_time = time.time()
message = "Hello"
key = RSA.generate(1024)

r = random.StrongRandom().randint(1,key.n-1)
sign = key.sign(message,r)

if key.verify(message, sign):
    print "OK"
else:
     print "Incorrect signature"
     
print("--- %s seconds ---" %(time.time() - start_time))
