# This function takes two sorted lists and merges them into one sorted list
# Input: L1,L2 - Two sorted lists
# Output: L - One sorted list
def merge(L1,L2):
    L = [] # Array where the sorted list will be stored

    while len(L1) != 0 and len(L2) != 0:
        # While L1 and L2 are both nonempty 
        if L1[0] < L2[0]:
            # If L1 contains the 1st smaller element, remove element and add to end of L
            print(L1[0],end="")
            print('<', end = "")
            print(L2[0], end = "")
            print()
            L.append(L1[0])
            L1.remove(L1[0])
        else:
            # If L2 contains the 1st smaller element, remove element and add to end of L
            print(L2[0], end = "")
            print('<', end = "")
            print(L1[0], end = "")
            print()
            L.append(L2[0])
            L2.remove(L2[0])

    while len(L1) != 0:
        L.append(L1[0])
        L1.remove(L1[0])

    while len(L2) != 0:
        L.append(L2[0])
        L2.remove(L2[0])

    return L

# This function takes an unordered list and transforms it to an ordered list
# Input: An unordered list
# Returns: A ordered list (ascending)
def mergeSort(L):
    if len(L) > 1:
        # Check if the size of the list is greater than 1
        m = len(L) // 2 # m = floor(n/2)
        L1 = L[:m] # L1 = a1, a2, ..., am
        L2 = L[m:]# L2 = am+1, am+2, ..., an
        L = merge(mergeSort(L1), mergeSort(L2))
    return L


print(mergeSort([1, 3, 2, 7, 12, 14, 5, 9]))