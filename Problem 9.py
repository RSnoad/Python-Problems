from math import sqrt


# Function to find pythagorean triplet that totals input (uses pTriple function).
def tripleTotal(total):
    for a in range(1, total):
        for b in range(a + 1, total):
            # Could also write as c = total - a - b, might be more efficient?
            c = sqrt(a ** 2 + b ** 2)
            if pTriple(a, b, c):
                if a + b + c == total:
                    print(a, b, int(c))
                    print(int(a * b * c))


# Function to determine if 3 integers are a pythagorean triple.
def pTriple(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

tripleTotal(12)
tripleTotal(1000)















