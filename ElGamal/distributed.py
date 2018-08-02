from Crypto.PublicKey.pubkey import *
from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util import number

#Calculation Node
class Node:
    #Generate Key
    def genSK(self, p):
        s = number.getRandomRange(2, p-1)
        return s

    def genPK(self, p, g, s):
        y = pow(g, s, p)
        return y
class Owner:
    #Data Owner
    def multPK(self, p, g, message, *pb):
            #generate Publickey
        y = 1
        for x in pb:
            y = x * y

        r = number.getRandomRange(1, p-1)
        enc = (pow(g,r,p), message * pow(y,r,p))
        return enc

    def enc(self, p, g, y, message):
        enc = (pow(g,r,p), message * pow(y,r,p))
        return enc

    def multiple(self, p ,*enc):
        c1 = 1
        c2 = 1
        for x in enc:
            c1 = c1 * x[0]
            c2 = c2 * x[1]
        mult = (c1 % p, c2 % p)
        return mult

    def partdec(self, multdec, s):
            # dec = (pow(multdec[0],s,p), multdec[1])
        dec = pow(multdec[0], s, p)
        return dec
class ServiceProvider:
    #Service Provider
    def reconstruct(self, mult, p, *dec):
        cipher = 1
        for x in dec:
            cipher *= x
        dec = pow(cipher, p-2, p)
        result = (dec * mult[1]) % p
        return result




#
# message1 = 100
# message2 = 10
#
p = number.getPrime(160 , Random.new().read)
g = number.getRandomRange(3, p-1)


node1 = Node()
sk1 = node1.genSK(p)
pk1 = node1.genPK(p,g,sk1)

node2 = Node()
sk2 = node2.genSK(p)
pk2 = node2.genPK(p,g,sk2)

print pk1, pk2

owner1 = Owner()
owner2 = Owner()

message1 = 12
message2 = 2

enc1 = owner1.enc(p,g,pk1,message1)
enc2 = owner2.enc(p,g,pk2,message2)
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
