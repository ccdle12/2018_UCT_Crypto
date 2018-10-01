import os, hashlib, random, Crypto.PublicKey.RSA
from rst01 import ring

size = 4
msg1, msg2 = 'hello', 'world!'

def _rn(_):
    return Crypto.PublicKey.RSA.generate(1024, os.urandom)

key = map(_rn, range(size))
r = ring(key)
for i in range(size):
    s1 = r.sign(msg1, i)
    s2 = r.sign(msg2, i)
    assert r.verify(msg1, s1) and r.verify(msg2, s2) and not r.verify(msg1, s2)