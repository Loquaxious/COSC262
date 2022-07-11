from counting_sort import *

def radix_sort(numbers, d):
    """Takes a sequence of natural numbers and uses counting sort iterativley 
    to sort the sequence upto the d-th digit from the right"""
    for i in range(0, d):
        key = lambda x: ((x // 10**i) % 10)
        numbers = counting_sort(numbers, key)
    return numbers
        
        
print(radix_sort([329, 457, 657, 839, 436, 720, 355], 3))
print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1))
print(radix_sort([329, 457, 657, 839, 436, 720, 355], 2))