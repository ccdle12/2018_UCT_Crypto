from Crypto.Random import random
from Crypto.Util import number

#Generate Private Key for Each Player
def genParameter(security):
    prime = number.getPrime(2 * security)
    generator = number.getRandomRange(1, prime-1)

    return prime, generator

# def genPrivKey(prime, shares):
#     sk = []
#     for i in range(shares):
#         sk.append(number.getRandomRnage(2, prime-1))
    
#     return sk

def genPrivKey(prime):
    sk = number.getRandomRange(2, prime - 1)

    return sk

# Generate Public Key for Each Player
# def genPubKey(prime, generator, sk, shares):
#     pubKey = []
#     for i in range(shares):
#         pubKey.append(pow(generator, sk, prime))
    
#     return pubKey

def genPubKey(prime, generator, sk):
    pubKey = pow(generator, sk, prime)

    return pubKey

# Encryption
def enc(prime, generator, msg, *pubKey):
    multPubKey = 1

    for i in pubKey:
        multPubKey *= i

    r = number.getRandomRange(1, prime-1)

    ctxt = (pow(generator, r, prime), msg * pow(multPubKey, r, prime))

    return ctxt

# Multiplication for Two Ciphertexts
def mult(p ,*ctxt):
    c1 = 1
    c2 = 1
    for x in ctxt:
        c1 = c1 * x[0]
        c2 = c2 * x[1]
    multCtxt = (c1 % p, c2 % p)

    return multCtxt

# Partial Decryption for Each Player
def partDec(ctxt, prime, sk):
    partMsg = pow(ctxt[0], sk, prime)

    return partMsg

# Reconstruction Message
def reconstruct(ctxt, prime, *partMsg):
    cipher = 1
    for x in partMsg:
        cipher *= x

    partMsg = pow(cipher, prime-2, prime)
    msg = (partMsg * ctxt[1]) % prime

    return msg

# #### Parameter
# security = 80
# shares = 5

# msg1, msg2 = number.getRandomRange(1, 100), number.getRandomRange(1, 100)

# #### Key Generation
# prime, generator = genParameter(security)

# sk, pk = [], []

# for i in range(shares):
#     sk.append(genPrivKey(prime))
#     pk.append(genPubKey(prime, generator, sk[i]))

# #### Encryption
# ctxt1, ctxt2 = enc(prime, generator, pk, msg1), enc(prime, generator, pk, msg2)


# #### Decryption
# partMsg1, partMsg2 = [], []

# for i in range(shares):
#     partMsg1.append(partDec(ctxt1, prime, sk[i]))
#     partMsg2.append(partDec(ctxt2, prime, sk[i]))

# decMsg1 = reconstruct(ctxt1, prime, partMsg1)
# decMsg2 = reconstruct(ctxt2, prime, partMsg2)
# assert decMsg1 == msg1, "Encryption or Decryption is wrong!"
# assert decMsg2 == msg2, "Encryption or Decryption is wrong!"

# #### Multiplication
# partMultMsg = []

# multCtxt = mult(prime, ctxt1, ctxt2)

# for i in range(shares):
#     partMultMsg.append(partDec(multCtxt, prime, sk[i]))

# multMsg = reconstruct(multCtxt, prime, partMultMsg)
# assert multMsg == msg1 * msg2, "Multiplication is wrong!"