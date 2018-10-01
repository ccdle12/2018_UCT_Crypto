from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Util import number
from fractions import gcd

class signer:
    def keygen(self, key):
        return key
        
    def sign(self, t, key):
        s = pow(t, key.d, key.n)
        s1 = key.sign(123, random.StrongRandom().randint(1, key.n-1))
        return s ,s1

class verifier:
    def multinv(self, modulus, value):
        x, lastx = 0, 1
        a, b = modulus, value
        while b:
            a, q, b = b, a // b, a % b
            x, lastx = lastx - q * x, x
        result = (1 - lastx * modulus) // value
        if result < 0:
            result += modulus
        assert 0 <= result < modulus and value * result % modulus == 1
        return result

    def getRandom(self, key):
        r= number.getRandomRange(1,key.n-1)
        result = False
        while(result):
            r = number.getRandomRange(1,key.n-1)
            if(gcd(r,key.n)==1):
                result = True
        return r

    def blindmsg(self, msg, key, r):
        t = pow(r,key.e,key.n) * msg % key.n
        return t

    def unblindmsg(self, s, r, key):
        r = self.multinv(key.n, r)
        msg =  (s*r) % key.n
        return msg

    def verify(self, msg, original, key):
        result = 'false'
        verify = pow(msg, key.e, key.n)

        if (verify == original):
            result = 'true'
        else:
            result = 'false'
        return result

        # print key.verify(original, msg)

    

key = RSA.generate(1024)
s = signer()
v = verifier()

pubkey = s.keygen(key)
message = 123
r = v.getRandom(pubkey)
t = v.blindmsg(message, pubkey, r)

s, s1 = s.sign(t, key)
msg = v.unblindmsg(s, r, pubkey)


print v.verify(msg, message, pubkey)





# message = 123
# key = keygen()
# r = getRandom(key)
# t = blindmsg(message, key, r)
# s, s1 = sign(t, key)
# msg = unblindmsg(s, r, key)
# print s, s1, msg
# print key.verify(msg, s)

# def __init():
#     message = 123
#     key = keygen()
#     r = getRandom(key)
#     t = blindmsg(message, key, r)
#     s, s1 = sign(t, key)
#     msg = unblindmsg(s, r, key)
#     print s, s1
#     print key.verify(msg, s)

#     # print unblindmsg(s, r, key);
#     # unblind = unblindmsg(s, r, key)
#     # print unblind
#     # print verify(unblind, message, key)
