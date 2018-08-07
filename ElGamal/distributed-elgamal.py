from Crypto.PublicKey.pubkey import *
from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util import number

#obj=ElGamalobj()

#Generate Private Key for Each Player
def genPrivkey(p, g):
    sk = number.getRandomRange(2, p-1)
    return sk

#Generate Public Key for Each Player
def genPubkey(p, g, s):
    pubKey = pow(g, s, p)
    return pubKey

#Multiplying All Public Key for Each Player
def multPubKey(p, *pk):
    multPubKey = 1
    for x in pk:
        multPubKey = x * multPubKey

    multPubKey %= p

    return multPubKey

#Encryption
def enc(p, g, y, msg):
    r = number.getRandomRange(1, p-1)
    ctxt = (pow(g,r,p), msg * pow(y,r,p))

    return ctxt

#Multiplication for Two Ciphertexts
def mult(p ,*ctxt):
    c1 = 1
    c2 = 1
    for x in ctxt:
        c1 = c1 * x[0]
        c2 = c2 * x[1]
    multCtxt = (c1 % p, c2 % p)
    return multCtxt

#Partial Decryption for Each Player
def partDec(ctxt, sk):
    dec = pow(ctxt[0], sk, p)
    return dec

def reconstruct(ctxt, p, *partMsg):
    cipher = 1
    for x in partMsg:
        cipher *= x

    partMsg = pow(cipher, p-2, p)
    msg = (partMsg * ctxt[1]) % p
    return msg