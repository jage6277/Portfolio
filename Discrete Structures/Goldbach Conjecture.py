import math


# Function to check if a value is prime
# Input: positive integer N
# output: True if integer is prime, False otherwise
def checkPrime(N):
    if (N == 1):
        # Edge case
        return False
    for i in range(2,N):
        # Even case
        if N % i == 0:
            return False
    return True

# Function that finds values based off of the Goldbach Conjecture
# Input: positive, even integer N
# Output: Two positive, prime numbers that add up to the even number N
def goldbachCheck(N):
    # Look through values 2 - N-1 
    for i in range(2, N-1):
        # Check if values are both prime
        if checkPrime(i) and checkPrime(N-i):
            # If prime, return the results
            return (i, N-i)
    

# Test
print(goldbachCheck(12))