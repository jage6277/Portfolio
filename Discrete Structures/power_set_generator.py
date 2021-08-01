import math;
from itertools import combinations

# This Function generates the power set of a set
# Input: A set of numbers ( A, list data type)
# Return: Power set of the input set ( P(A), list data type)
def powerSet(A):
    sizeA = len(A) # Find size of set A and P(A)
    sizePA = 2 ** sizeA # Size of P(A)

    # Counters
    i = 0
    j = 0

    PA = list() # List for P(A) 

    # Generate P(A)
    for i in range(sizeA+1):
        for element in combinations(A,i):
            PA.append(element)

    return PA

# Example
A = [1,2,3]
print (powerSet(A))