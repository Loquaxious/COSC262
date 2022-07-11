def counting_sort(iterable, key):
    """Takes an array of values and sorts them based based on the key"""
    positions = key_positions(iterable, key)
    return sorted_array(iterable, key, positions)


def sorted_array(seq, key, positions):
    """Takes a sequence, a key function, and an array of positions and produces 
    an array containing elemsnts of seq sorted according to the key function"""
    b = [None for _ in range(len(seq))]
    for a in seq:
        b[positions[key(a)]] = a
        positions[key(a)] = positions[key(a)] + 1
    return b


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