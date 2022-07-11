def concat_list(strings):
    """Recursively Concatenates Strings"""
    the_string = ''
    if len(strings) == 0:
        return the_string
    else:
        return strings[0] + concat_list(strings[1:])
    
ans = concat_list(['a', 'hot', 'day'])
print(ans)

ans = concat_list(['x', 'y', 'z'])
print(ans)

print(concat_list([]))