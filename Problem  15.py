# Find the number of possible routes from top left to bottom right for an n x n grid, only by moving right or down.
from math import factorial

# Use Binomial coefficient formula for n choose r = n! / (r! = (n-r)!)
# Our n = 2 * size of grid as this is the total number of choices we need to make to reach the end.
# Our r = size of grid as this is the total number options to choose when getting all paths, i.e. choosing right
# eliminates a choice to go down.
def routes(n):
    print(int((factorial(2 * n)) / (factorial(n) * factorial(n))))


routes(20)