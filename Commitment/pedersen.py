from Crypto import Random
from Crypto.Random import random
from Crypto.Util import number

def generate(output):
        q = output[1]
        g = output[2]
        h = output[3]
        return q,g,h



class verifier:
    def setup(self):
        p = number.getPrime(160, Random.new().read)
        q = 2*p + 1
        g = number.getRandomRange(1, q-1)
        s = number.getRandomRange(1, q-1)
        h = pow(g,s,q)
        
        output = (p,q,g,h)
        return output

    def open(self, output, c, x, *r):
        result = "False"
        q,g,h = generate(output)

        sum = 0
        for i in r:
            sum += i

        print sum

        res = (pow(g,x,q) * pow(h,sum,q)) % q

        if(c == res):
            result = "True"
        return result  

    def mult(self, output, *com):
        mult = 1
        for x in com:
            mult *= x
        mult = mult % output[1]
        return mult
        
class prover: 
    def commit(self, output, x):
        q,g,h = generate(output)
        
        r = number.getRandomRange(1, q-1)
        c = (pow(g,x,q) * pow(h,r,q)) % q
        return c, r
    

v = verifier()
p = prover()

x = 500

output = v.setup()

c1, r1 = p.commit(output, x)
c2, r2 = p.commit(output, 100)

mul = v.mult(output, c1, c2)

# print v.open()

# result1 = v.open(output, c1, x, r1)
# result2 = v.open(output, c2, 100 , r2)

# print mult 
result = v.open(output, mul, x+100 , r1, r2)

# # print c
print result
