class Item:
    """An item to (maybe) put in a knapsack"""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
    def __repr__(self):
        return f"Item({self.value}, {self.weight})"
        
        
def max_value(items, capacity):
    """The maximum value achievable with a given list of items and a given
       knapsack capacity."""
    n = len(items)
    table = [[0 for _ in range(capacity + 1)] for __ in range(n + 1)]
    
    for i in range(n+1):
        for j in range(capacity+1):
            if i == 0:
                table[i][j] = 0
            elif i > 0 and items[i-1].weight > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(table[i-1][j], table[i-1][j-items[i-1].weight] \
                                  + items[i-1].value)
    return table[n][capacity]

# The example in the lecture notes
items = [Item(45, 3),
         Item(45, 3),
         Item(80, 4),
         Item(80, 5),
         Item(100, 8)]
print(max_value(items, 10))         
