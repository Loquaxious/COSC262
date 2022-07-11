import sys
sys.setrecursionlimit(2000)

class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"
        
def max_value(items, capacity):
    """Returns the maximum vlaue achievable with the given list of items
    and a knapsack of the given capacity""" 
    n = len(items)
    memo = {}

    def max_val(items, capacity, n):
        if (capacity, n) not in memo:
            if n == 0:
                memo[(capacity, n)] = 0
                return memo[(capacity, n)]
            elif items[n-1].weight > capacity:
                memo[(capacity, n)] = max_val(items, capacity, n-1)
                return memo[(capacity, n)]
            else:
                memo[(capacity, n)] = max(max_val(items, capacity, n-1), items[n-1].value \
                   + max_val(items, capacity - items[n-1].weight, n-1))
                return memo[(capacity, n)]
        else:
            return memo[(capacity, n)]
    
    return max_val(items, capacity, n)
    
    
# The example from the lecture notes
items = [
    Item(45, 3),
    Item(45, 3),
    Item(80, 4),
    Item(80, 5),
    Item(100, 8)]

print(max_value(items, 10))

# A large problem (500 items)
import random
random.seed(12345)  # So everyone gets the same

items = [Item(random.randint(1, 100), random.randint(1, 100)) for i in range(500)]
print(max_value(items, 500))