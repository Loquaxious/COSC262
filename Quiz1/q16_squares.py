def squares(data):
    """returns a new list that contains the squares of the numbers in data"""
    
    if len(data) == 0:
        return []
    else:
        return [data[0] * data[0]] + squares(data[1:])
    
print(squares([1, 13, 9, -11]))
    