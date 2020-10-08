# Find the starting number for this sequence, under 1 million, with the longest chain.

# Function that goes through the iterative sequence and returns the sequence as a list of integers.
def sequence(n):
    chain = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            chain.append(int(n))
        else:
            n = 3*n + 1
            chain.append(int(n))
    return chain

# Create variables for while counter and to store the longest known chain.
i = 2
longestChain = []

# Brute force (slow!) while loop used to find length of every chain for n < 1m, and update longestChain if needed.
while i < 1000000:
    if len(sequence(i)) > len(longestChain):
        longestChain = sequence(i)
    i += 1
    # Print to track progress (it takes a while).
    print(i)


print(longestChain)
print(longestChain[0])