import sys
sys.setrecursionlimit(100000)

def dumbo_func(data, start_index=0):
    """Takes a list of numbers and does weird stuff with it"""
    if start_index == len(data):
        return 0
    else:
        if (data[start_index] // 100) % 3 != 0:
            return 1 + dumbo_func(data, start_index + 1)
        else:
            return dumbo_func(data, start_index + 1)
        
        
# Simple test with short list.
# Original func works fine on this
data = [677, 90, 785, 875, 7, 90393, 10707]
print(dumbo_func(data))


for i in range(20):
    # Repeat enough times to ensure timeout on O(n^2)
    data = list(range(1000))
    your_ans = dumbo_func(data)
print("Yay!")