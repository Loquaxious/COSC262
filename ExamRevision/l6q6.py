def key_positions(seq, key):
    k = key(max(seq, key=lambda x:key(x)))
    c = [0 for _ in range(k+1)]
    for a in seq:
        c[key(a)] = c[key(a)] + 1
    csum = 0
    for i in range(k+1):
        c[i], csum = csum, csum + c[i]
    return c

print(key_positions([0, 1, 2], lambda x: x))
print(key_positions(range(-3,3), lambda x: x**2))
print(key_positions(range(1000), lambda x: 4))
print(key_positions([1] + [0] * 100, lambda x: x))