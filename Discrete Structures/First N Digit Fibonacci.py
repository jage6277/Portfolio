# This function prints the first value in the fibonacci sequence that has N digits
# Input: N (non-negative integer), i.e. the number of digits
# Output: First number in fibonacci sequence that has N digits 
def first_N_digit_Fib(N):
    # Initial Values
    F0 = 0
    F1 = 1
    # Loop until the Nth term is found
    while True:
        # Compute value of sequence
        F2 = F0 + F1
        # Update values for next iteration
        F0 = F1
        F1 = F2
        # if the sequence length is N, stop and return value
        if (len(str(F2)) == N):
            return F2
            

print(first_N_digit_Fib(3))