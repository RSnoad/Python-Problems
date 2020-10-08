# Find the 10,001st prime number
from math import sqrt

# Function to find the nth prime in list using the isPrime function below.
def nthPrime(n):
    i = 2
    primeList = []
    while len(primeList) < n:
        if isPrime(i):
            primeList.append(i)
        i += 1

    print(primeList[-1])


# Brute force method to check if a number is prime.
# Could also clean up to give error for certain input ( negatives, decimals etc)
def isPrime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

nthPrime(6)
nthPrime(10001)
