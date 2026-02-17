import random
import math

#This is purely for the base generqation, don't confuse with binary
basesTable = {
    0: -45,
    1: 45,
    2: 0,
    3: 90
}

keyLength = 15
debugStats = False

def rng(n,m):
    return [random.randint(0,m) for i in range(n)]

def generate_basis(baseList):
    basis = []
    for base in baseList:
        basis.append(basesTable[base])
    return basis

def overlap(theta,phi):
    if theta == phi:
        return 0
    elif abs(theta) > abs(phi):
        return abs(theta) - abs(phi)
    elif theta == -phi:
        return 90
    else:
        return abs(phi) - abs(theta)

def generate_overlaps_list(a,b,length):
    overlaps_list = []
    for i in range(length):
        overlaps_list.append(overlap(a[i],b[i]))
    return overlaps_list

def probability(angle):
    return 1 - (math.cos(math.radians(angle)) ** 2)

def generate_probabilities(oList):
    probabilities_list = []
    for o in oList:
        probabilities_list.append(probability(o))
    return probabilities_list

def bob_measure(pList,aStr):
    bobReceive = []
    for bit in range (len(aStr)):
        if bit == 0:
            if random.random() < pList[bit]:
                bobReceive.append(0)
            else:
                pass
        else:
            if random.random() < pList[bit]:
                bobReceive.append(1)
            else:
                pass
    return bobReceive

if debugStats:
    print("Alice basis:",aliceBasis)
    print("Alice bitstring:",aliceStr)
    print("Bob basis:",bobBasis)
    print("Angle difference:",abOverlaps)
    print("Associated probabilities:",abProbabilities)
    print("Result:",result)
    print("Result length:",len(result))


