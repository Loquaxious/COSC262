def my_enumerate(items, start_index=0):
    """Returns a numbered list of tuples"""
    
    if start_index >= len(items):
        return []
    else:
        return [(start_index, items[start_index])] + my_enumerate(items, start_index+1)
    
    
ans = my_enumerate([10, 20, 30])
print(ans)
ans = my_enumerate(['dog', 'pig', 'cow'])
print(ans)
ans = my_enumerate([])
print(ans)