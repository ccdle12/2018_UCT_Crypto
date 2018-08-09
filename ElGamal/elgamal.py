from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util import number

def genKey():
    key = ElGamal.generate(160, Random.new().read)
    
    return key

def enc(key, msg):
    p = key.p
    r = number.getRandomRange(1, p-1)
    ctxt = key.encrypt(msg, r)

    return ctxt

def mult(p, *ctxt):
    c1 = 1
    c2 = 1
    for x in ctxt:
        c1 = c1 * x[0]
        c2 = c2 * x[1]
    multCtxt = (c1 % p, c2 % p)
    return multCtxt