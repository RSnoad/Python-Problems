from math import gcd
from functools import reduce
# print(reduce(lambda a, b: a * b / gcd(a, b), range(1, 21)))

# Function to find greatest common divisor using Euclid's algorithm (needed for lcm function)
# #
# def gcd(i, j):
#     while j > 0:
#         i, j = j, i % j
#     return i


print(gcd(456, 654))

# Function to find lowest common multiple using Euclid's for two numbers
def lcm(i, j):
    return i * j // gcd(i,j)


print(lcm(15, 12))


#Function to find lcm for list of numbers
def lcmlist(*args):
    return reduce(lcm, args)

print(lcmlist(*range(1, 20)))