from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util import number

def keyGen(security):
    key = ElGamal.generate(2 * security, Random.new().read)
    
    return key


def enc(key, msg):
    p = key.p
    r = number.getRandomRange(1, p-1)
    ctxt = key.encrypt(msg, r)

    return ctxt


def dec(key, ctxt):
    msg = key.decrypt(ctxt)

    return msg


def mult(p, *ctxt):
    c1 = 1
    c2 = 1
    for x in ctxt:
        c1 = c1 * x[0]
        c2 = c2 * x[1]
    multCtxt = (c1 % p, c2 % p)
    return multCtxt


security = 80
msg1, msg2 = number.getRandomRange(1, 100), number.getRandomRange(1, 100)

key = keyGen(security)
ctxt1, ctxt2 = enc(key, msg1), enc(key, msg2)

decMsg1, decMsg2 = dec(key, ctxt1), dec(key, ctxt2)
assert decMsg1 == msg1, "Encryption or Decryption is wrong!"
assert decMsg2 == msg2, "Encryption or Decryption is wrong!"

multCtxt = mult(key.p, ctxt1, ctxt2)
multMsg = dec(key, multCtxt)
assert multMsg == msg1 * msg2, "Multiplication is wrong!"