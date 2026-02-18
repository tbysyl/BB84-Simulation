from bb84 import *

numRuns = int(input("How many runs to average?: "))
keyLength = int(input("How many bits to send?: "))
debugStats = True
total = 0
eve = True

for i in range(numRuns):
    aliceBasis = generate_basis(rng(keyLength,3))
    bobBasis = generate_basis(rng(keyLength,3))

    if eve:
        #Eve intercepts Alice's bits
        eveBasis = generate_basis(rng(keyLength,3))
        aeOverlaps = generate_overlaps_list(aliceBasis,eveBasis,keyLength)
        aeProbabilities = generate_probabilities(aeOverlaps)
        aliceStr = rng(keyLength,1)
        eveResult = measure(aeProbabilities,aliceStr)


        #Eve hands off bits she received
        ebOverlaps = generate_overlaps_list(bobBasis,eveBasis,keyLength)
        ebProbabilities = generate_probabilities(ebOverlaps)
        bobResult = measure(ebProbabilities,eveResult)
        total += len(bobResult)

    else:
        abOverlaps = generate_overlaps_list(aliceBasis,bobBasis,keyLength)
        abProbabilities = generate_probabilities(abOverlaps)
        aliceStr = rng(keyLength,1)
        bobResult = measure(abProbabilities,aliceStr)
        total += len(bobResult)

    if debugStats:
        if eve:
            print(f"[{i+1}]")
            print("Alice basis:",aliceBasis)
            print("Alice bitstring:",aliceStr)
            print("Eve basis:",eveBasis)
            print("Eve sends:",eveResult)
            print("Bob basis:",bobBasis)
            print("Result:",bobResult)
            print("Result length:",len(bobResult))
            print("-" * 50)
        else:
            print(f"[{i+1}]")
            print("Alice basis:",aliceBasis)
            print("Alice bitstring:",aliceStr)
            print("Bob basis:",bobBasis)
            #print("Angle difference:",abOverlaps)
            #print("Associated probabilities:",abProbabilities)
            print("Result:",bobResult)
            print("Result length:",len(bobResult))
            print("-" * 50)

print("Mean key length: ",total / numRuns)

