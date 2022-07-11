def sorted_array(seq, key, positions):
    b = [None for _ in range(len(seq))]
    for a in seq:
        b[positions[key(a)]] = a
        positions[key(a)] = positions[key(a)] + 1
    return b


def key_positions(seq, key):
    k = key(max(seq, key=lambda x:key(x)))
    c = [0 for _ in range(k+1)]
    for a in seq:
        c[key(a)] = c[key(a)] + 1
    csum = 0
    for i in range(k+1):
        c[i], csum = csum, csum + c[i]
    return c

print(sorted_array([3, 1, 2], lambda x: x, [0, 0, 1, 2]))
print(sorted_array([3, 2, 2, 1, 2], lambda x: x, [0, 0, 1, 4]))
print(sorted_array([100], lambda x: x, [0]*101))

"""Counting Sort"""
import operator

def counting_sort(iterable, key):
    positions = key_positions(iterable, key)
    return sorted_array(iterable, key, positions)
    
objects = [("a", 88), ("b", 17), ("c", 17), ("d", 7)]

key = operator.itemgetter(1)
print(", ".join(object[0] for object in counting_sort(objects, key)))