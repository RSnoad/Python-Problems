# Largest palindromic number that is factor of 3 digit numbers


# text = 'thing to reverse'[::-1]
# print (text)

# Function to check if number is a palindrome
def palindrome(n):
    return str(n) == str(n)[::-1]


# Brute forcing by checking every multiplication combo and adding palindromes to a list.
palindromeList = []
for firstMultiple in range (100, 1000):
    for secondMultiple in range (100, 1000):
        i = firstMultiple * secondMultiple

        # True is implied so can be shortened
        if palindrome(i):
            palindromeList.append(i)

print (max(palindromeList))
