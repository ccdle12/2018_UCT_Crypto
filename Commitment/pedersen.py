from Crypto import Random
from Crypto.Random import random
from Crypto.Util import number

class verifier:
    def setup(self):
        p = number.getPrime(160, Random.new().read)
        q = 2*p + 1
        g = number.getRandomRange(1, q-1)
        s = number.getRandomRange(1, q-1)
        h = pow(g,s,q)
        
        output = (p,q,g,h)
        return output

    def open(self, output, c, x, r):
        result = "False"
        q = output[1]
        g = output[2]
        h = output[3]
        
        r = pow(g,x,q) * pow(h,r,q)
        if(c == r):
            result = "True"
        return result  

class prover: 
    def commit(self, output, x):
        q = output[1]
        g = output[2]
        h = output[3]
        
        r = number.getRandomRange(1, q-1)
        c = pow(g,x,q) * pow(h,r,q)
        return c



# output = setup()
# print output[0]