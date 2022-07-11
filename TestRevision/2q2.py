def cycle_length(n):
    if n == 1:
        return 1
    else:
        if n%2 == 0:
            return 1 + cycle_length(n/2)
        else:
            return 1 + cycle_length(3*n+1)

print(cycle_length(22))
