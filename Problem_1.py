# Find sum of all multiples of 3 & 5 below 1000
# total = 0
# for i in range(1000):
#     if i % 3 == 0 or i % 5 == 0:
#         total += i
#
# print(total)

def sumOfNaturalsBelow(n):
    total = 0
    for i in range(n):
        if multipleOfInteger(i, 3) or multipleOfInteger(i, 5):
            total += i
    return total

# def multipleOfThree(n):
#     if n % 3 == 0:
#         return True
#
# def multipleOfFive(n):
#     if n % 5 == 0:
#         return True

def multipleOfInteger(n, divisor):
    if n % divisor == 0:
        return True
    return False
