from bb84test import *

numRuns = int(input("Enter the number of runs to average: "))
length = int(input("Enter number of initial bits: "))
eveToggle = True

keySum = 0
qberSum = 0

for i in range(numRuns):
    result = simulate(length,eveToggle)
    keySum += len(result[0])
    qberSum += result[3]

avgLength = keySum / numRuns
avgQber = qberSum / numRuns

print(f"{avgLength} | {avgQber}%")
