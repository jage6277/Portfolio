# This function will print the Nth term defined by the following recurrence relation:
    # a(0) = 1
    # a(1) = 2
    # a(N) = n^2 * a(n-1) - a(n-2)
# Input: nonnegative integer N
# Output: Nth term of sequence (integer)
def recurrence_relation(N):
    if N == 0:
        return 1
    elif N == 1:
        return 2
    return N*N*recurrence_relation(N-1) - recurrence_relation(N-2)

# Test
print(recurrence_relation(3))