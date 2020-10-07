from math import sqrt


# Function to find largest prime factor using brute force division method.
def largestPrime(n):
    i = 2
    # Only need to check up to the square root of the number we are checking, as with the isPrime function.
    while i < sqrt(n):
        if n % i != 0:
            i += 1
        else:
            n = n / i
    print(int(n))


largestPrime(600851475143)

