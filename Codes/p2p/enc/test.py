from sys import argv
import distributed

info = argv[1]

if(info == 'genkey'):
    prime = int(argv[2])
    generator = int(argv[3])

    sk = distributed.genPrivKey(prime)
    pk = distributed.genPubKey(prime, generator, sk)

    print(prime, generator, pk,sk)

elif(info == 'genparam'):
    prime, generator = distributed.genParameter(160)
    print(prime, generator)

elif(info == 'enc'):
    # prime, generator, pk, msg
    prime = int(argv[2])
    generator = int(argv[3])
    pk = int(argv[4])
    msg = int(argv[5])

    ctxt = distributed.enc(prime, generator, msg, pk)

    print(ctxt)
