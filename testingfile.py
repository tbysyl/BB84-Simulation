from bb84 import *

numRuns = int(input("How many runs to average?: "))
keyLength = int(input("How many bits to send?: "))
total = 0
debugStats = True

for i in range(numRuns):
    aliceBasis = generate_basis(rng(keyLength,3))
    bobBasis = generate_basis(rng(keyLength,3))
    abOverlaps = generate_overlaps_list(aliceBasis,bobBasis,keyLength)
    abProbabilities = generate_probabilities(abOverlaps)
    aliceStr = rng(keyLength,1)
    result = bob_measure(abProbabilities,aliceStr)
    total += len(result)

    if debugStats:
        print(f"[{i+1}]")
        print("Alice basis:",aliceBasis)
        print("Alice bitstring:",aliceStr)
        print("Bob basis:",bobBasis)
        print("Angle difference:",abOverlaps)
        print("Associated probabilities:",abProbabilities)
        print("Result:",result)
        print("Result length:",len(result))
        print("-" * 50)

print("Mean key length: ",total / numRuns)

