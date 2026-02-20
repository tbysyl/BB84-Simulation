import math
import random

states = {
    ("Z",0): 0,
    ("Z",1): 90,
    ("X",0): 45,
    ("X",1): -45,
}

def rng_bits(n):
    bitString = []
    for i in range(n):
        bitString.append(random.randint(0,1))
    return bitString

def rng_basis(n):
    basis = []
    for i in range(n):
        basis.append(random.choice(("Z","X")))
    return basis

def encoding(basis,bits):
    angles = []
    for i in range(len(basis)):
        angles.append(states[(basis[i],bits[i])])
    return angles
        
def measure(received,bBasis):
    measured = []
    for i in range(len(received)):
        if bBasis[i] == "Z":
            if received[i] == 0:
                measured.append(0)
            elif received[i] == 90:
                measured.append(1)
            else:
                measured.append(random.randint(0,1))
        else:
            if received[i] == 45:
                measured.append(0)
            elif received[i] == -45:
                measured.append(1)
            else:
                measured.append(random.randint(0,1))
    return measured

def matching_indices(aBasis,bBasis):
    indices = []
    for i in range(len(aBasis)):
        if aBasis[i] == bBasis[i]:
            indices.append(i)
    return indices

def sifting(unsifted,indices): #"Afraid to grade; Wouldn't it be fun?"
    sifted = []
    for i in indices:
        sifted.append(unsifted[i])
    return sifted

def count_errors(alice_key,bob_key):
    errors = 0
    for i in range(len(alice_key)):
        if alice_key[i] != bob_key[i]:
            errors += 1
    return errors

def calculate_qber(errors,length):
    return (errors / length) * 100

def simulate(keyLength,eve):
    #Create the bases and message. The message is random here because it is not important.
    aBasis = rng_basis(keyLength)
    bBasis = rng_basis(keyLength)
    aBits = rng_bits(keyLength)
    aliceMsg = encoding(aBasis,aBits)

    if eve:
        #Eve creates basis, intercepts, and hands off
        eBasis = rng_basis(keyLength)
        eveMeasured = measure(aliceMsg,eBasis)
        eveMsg = encoding(eBasis,eveMeasured)
        
        #Bob reads Eve's bits, believing they are from Alice
        bobMeasured = measure(eveMsg,bBasis)
    else:
        bobMeasured = measure(aliceMsg,bBasis)

    indices = matching_indices(aBasis,bBasis)
    bobSifted = sifting(bobMeasured,indices)
    aliceSifted = sifting(aBits,indices)
    errorCount = count_errors(aliceSifted,bobSifted)
    qber = calculate_qber(errorCount,len(aliceSifted))

    return bobSifted,aliceSifted,errorCount,qber

