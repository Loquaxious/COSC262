def radix_sort(numbers, d):
    for i in range(1, d+1):
        numbers = counting_sort(numbers, lambda x: x % (10 ** i))
    return numbers


def counting_sort(iterable, key):
    positions = key_positions(iterable, key)
    return sorted_array(iterable, key, positions)


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

print(radix_sort([329, 457, 657, 839, 436, 720, 355], 3))
print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1))
print(radix_sort([329, 457, 657, 839, 436, 720, 355], 2))
