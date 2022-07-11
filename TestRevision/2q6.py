import sys
sys.setrecursionlimit(100000)

def dumbo_func(data, n=None):
    """Takes a list of numbers and does weird stuff with it"""
    if n == None:
        n = len(data)
    if n == 0:
        return 0
    else:
        if (data[n-1] // 100) % 3 != 0:
            return 1 + dumbo_func(data, n-1)
        else:
            return dumbo_func(data, n-1)
        
# Simple test with short list.
# Original func works fine on this
data = [677, 90, 785, 875, 7, 90393, 10707]
print(dumbo_func(data))