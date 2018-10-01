from Crypto import Random
from Crypto.Random import random
from Crypto.Util import number

def generate(param):
        q = param[1]
        g = param[2]
        h = param[3]
        return q,g,h

class verifier:
    def setup(self, security):
        p = number.getPrime(2 * security, Random.new().read)
        q = 2*p + 1
        g = number.getRandomRange(1, q-1)
        s = number.getRandomRange(1, q-1)
        h = pow(g,s,q)
        
        param = (p,q,g,h)
        return param

    def open(self, param, c, x, *r):
        result = "False"
        q,g,h = generate(param)

        sum = 0
        for i in r:
            sum += i

        res = (pow(g,x,q) * pow(h,sum,q)) % q

        if(c == res):
            result = "True"
        return result  

    def add(self, param, *cm):
        addCM = 1
        for x in cm:
            addCM *= x
        addCM = addCM % param[1]
        return addCM
        
class prover: 
    def commit(self, param, x):
        q,g,h = generate(param)
        
        r = number.getRandomRange(1, q-1)
        c = (pow(g,x,q) * pow(h,r,q)) % q
        return c, r
    

security = 80
msg1 = 500
msg2 = 100

v = verifier()
p = prover()

param = v.setup(security)

c1, r1 = p.commit(param, msg1)
c2, r2 = p.commit(param, msg2)

addCM = v.add(param, c1, c2)

# print v.open()

# result1 = v.open(param, c1, x, r1)
# result2 = v.open(param, c2, 100 , r2)

# print add 
result = v.open(param, addCM, msg1 + msg2 , r1, r2)

# # print c
print result
