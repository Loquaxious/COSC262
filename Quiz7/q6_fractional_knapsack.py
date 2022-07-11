def fractional_knapsack(capactiy, items):
    """Returns the maximum achieveable value obtainable with a knapsack
    of the given capacity and a given list of items, each represented by
    a tuple (name, value, weight)"""
    
    sorted_items = sorted(items, key=lambda item: item[1] / item[2], reverse=True)
    current_capacity = 0
    value = 0
    
    for item in sorted_items:
        if (current_capacity + item[2]) <= capactiy:
            current_capacity += item[2]
            value += item[1]
        else:
            frac = capactiy - current_capacity
            value += (item[1] * (frac/item[2]))
            break
    
    return value
    
    
# The example from the lecture notes
items = [
    ("Chocolate cookies", 20, 5),
    ("Potato chips", 15, 3),
    ("Pizza", 14, 2),
    ("Popcorn", 12, 4)]
print(fractional_knapsack(9, items))