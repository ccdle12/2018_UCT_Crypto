from Crypto.PublicKey.pubkey import *
from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util import number

#obj=ElGamalobj()

#Generate Key
def genPrivkey(p, g):
    s = number.getRandomRange(2, p-1)
    return s

def genPubkey(p, g, s):
    y = pow(g, s, p)
    return y

def multPub(p, g, message, *pb):
    #generate Publickey
    y = 1
    for x in pb:
        y = x * y

    r = number.getRandomRange(1, p-1)
    enc = (pow(g,r,p), message * pow(y,r,p))
    return enc

def enc(p, g, y, message):
    enc = (pow(g,r,p), message * pow(y,r,p))
    return enc

def mult(p ,*enc):
    c1 = 1
    c2 = 1
    for x in enc:
        c1 = c1 * x[0]
        c2= c2 * x[1]
    mult = (c1 % p, c2 % p)
    return mult

def partdec(multdec, s):
    # dec = (pow(multdec[0],s,p), multdec[1])
    dec = pow(multdec[0], s, p)
    return dec

def reconstruct(mult, p, *dec):
    cipher = 1
    for x in dec:
        cipher *= x
    dec = pow(cipher, p-2, p)
    result = (dec * mult[1]) % p
    return result

# message1 = 100
# message2 = 10
#
# p = number.getPrime(160 , Random.new().read)
# g = number.getRandomRange(3, p-1)
#
# # node
# pk1 = genPrivkey(p,g)
# pk2 = genPrivkey(p,g)
#
# pb1 = genPubkey(p,g, pk1)
# pb2 = genPubkey(p,g, pk2)
# # data owner
# enc1 = multPub(p, g, message1, pb1, pb2,)
# enc2 = multPub(p, g, message2, pb1, pb2,)
# # node
# dec1 = mult(p, enc1, enc2)
# dec2 = mult(p, enc1, enc2)
#
# part1 = partdec(dec1, pk1)
# part2 = partdec(dec1, pk2)
#
# result = reconstruct(dec1,p, part1, part2,)
#
# print result
#







#
#
# message1 = 3
# message2 = 2
# #n = input("NUMBER_OF_NODE" )
# p = number.getPrime(160, Random.new().read)
# g = number.getRandomRange(1, p-1)
#
# print p,g
#
# s1 = number.getRandomRange(1, p-1)
# s2 = number.getRandomRange(1, p-1)
# s3 = number.getRandomRange(1, p-1)
#
# y1 = pow(g, s1)
# y2 = pow(g, s2)
# y3 = pow(g, s3)
#
# s = s1 + s2+ s3
# y = y1 * y2 * y3
#
# key = ElGamal.construct((p,g,y,s))
#
# print key
#
# r = number.getRandomRange(1, p-1)
# enc = key.encrypt(message1, r)
#
# print enc
#
# #dec
# dec = key.decrypt(enc)
# print dec


# print(y1, y2, y3)
# y = y1*y2*y3
#
# pk = (p, g, y)
# print pk
#
# sk = s1 + s2 + s3
#
# print sk
#
# #ENC
#
# r = number.getRandomRange(1, p-1)
#
# print(r)
# enc = (pow(g,r), message1*pow(y,r))
#
# print(enc[0], enc[1])
#
# #print("result :  ",enc)
#
# dec1 = pow(enc[0],s1)
# dec2 = pow(enc[0],s2)
# dec3 = pow(enc[0],s3)
#
# decM = dec1 * dec2 * dec3
#
# dec = enc[1] / decM
# print dec
