# Find sum of primes below 2 million
from math import sqrt


# Function to sum primes below input n.
def sumPrime(n):
    i = 2
    sum = 0
    while i < n:
        if isPrime(i):
            sum += i
        i += 1
    print(sum)


# Function to determine if a number is prime - improved efficiency from previous version
# by only checking up to the square root +1 of a number.
# Still fairly inefficient - could find a better way! (look into sieve of eratosthenes)
def isPrime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


sumPrime(2000000)
