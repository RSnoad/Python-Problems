from math import sqrt


# Function for Fibonacci sequence using formula
def FSequence(n):
    return int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2**n * sqrt(5)))


# 33rd entry in sequence is the last number < 4 million. (Magic numbers, hard coded etc etc)
total = 0
for i in range(34):
    if FSequence(i) % 2 == 0:
        total += FSequence(i)

print(total)
