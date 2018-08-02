from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util import number

def genKey():
    key = ElGamal.generate(160, Random.new().read)
    return key

def genPK(key):
    publickey = key.publickey()
    return pulickey

def enc(key, message):
    p = key.p
    r = number.getRandomRange(1, p-1)
    enc = key.encrypt(message, r)
    return enc

def mult(p, *enc):
    c1 = 1
    c2 = 1
    for x in enc:
        c1 = c1 * x[0]
        c2 = c2 * x[1]
    mult = (c1 % p, c2 % p)
    return mult

def multdec(key, enc):
    multdec = key.decrypt(enc)
    return multdec
#
# message1 = 20
# message2 = 300
#
# key = genKey()
#
# p = key.p
#
# enc1 = enc(key, message1)
# enc2 = enc(key, message2)
#
# mult = mult(p, enc1, enc2)
# dec = multdec(key,mult)
# 
# print dec


#
# multdec = multdec(key, mult)
#
# print multdec

#
# #keygen
# key = ElGamal.generate(160, Random.new().read)
# p = key.p
# g = key.g
# y = key.y
# x = key.x
#
# #ENC
# r1 = number.getRandomRange(1, p-1)
# r2 = number.getRandomRange(1, p-1)
#
# enc1 = key.encrypt(message1, r1);
# enc2 = key.encrypt(message2, r2)
#
# #MULT
# a = enc1[0] * enc2[0]
# b = enc1[1] * enc2[1]
#
# Mult = (a,b)
#
# #DEC
# dec = key.decrypt(Mult);
# print dec
#
# #MULT


#
# h = SHA.new(message).digest()
# while 1:
#      k = random.StrongRandom().randint(1,key.p-1)
#      if GCD(k,key.p-1)==1: break
# sig = key.sign(h,k)
#
# if key.verify(h,sig):
#      print "OK"
# else:
#      print "Incorrect signature"
#
