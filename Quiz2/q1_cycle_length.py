def cycle_length(n):
    """Computes the Collatz cycle length"""
    length = 1
    if n == 1:
        return length
    elif n % 2 == 0:
        return 1 + cycle_length(n/2)
    else:
        return 1 + cycle_length(3*n+1)
    
print(cycle_length(23)) 