def perms(items, n=None):
    if n == None:
        n = len(items)
    if items == []:
        return [()] 
    elif n == 0:
        return [(item,) for item in items]
    else:
        