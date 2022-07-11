def key_positions(seq, key):
    """Takes a sequence and an key function, and returns an array such that the 
    i-th element of the array is the starting position of objects in seq whose 
    key is i"""
    k = key(seq[0])
    for i in range(1, len(seq)):
        if k < key(seq[i]):
            k = key(seq[i])
    c = [0 for _ in range(k+1)]
    
    for a in seq:
        c[key(a)] = c[key(a)] + 1
    
    sums = 0
    for i in range(k+1):
        c[i], sums = sums, sums+c[i]
    
    return c

print(key_positions([0, 1, 2], lambda x: x))
print(key_positions([2, 1, 0], lambda x: x))
print(key_positions([1, 2, 3, 2], lambda x: x))
print(key_positions([5], lambda x: x))
print(key_positions(range(-3,3), lambda x: x**2))
print(key_positions(range(1000), lambda x: 4))
print(key_positions([1] + [0] * 100, lambda x: x))