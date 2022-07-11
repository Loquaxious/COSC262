from collections import defaultdict 

def coins_reqd(value, coinage):
    """A version that doesn't use a list comprehension"""
    numCoins = [0] * (value + 1)
    pred = [0]
    for amt in range(1, value + 1):
        minimum = None
        minC = None
        for c in coinage:
            if amt >= c:
                coin_count = numCoins[amt - c] 
                if minimum is None or coin_count < minimum:
                    minimum = coin_count
                    minC = c
        pred.append(amt - minC)      
        numCoins[amt] = 1 + minimum
        
    backtrack = value
    d_dict = defaultdict(int)
    while backtrack != 0:
        d_dict[backtrack - pred[backtrack]] +=1
        backtrack = pred[backtrack]
        
    result = []
    for key, item in d_dict.items():
        result.append((key, item))
    return sorted(result, reverse=True)

print(coins_reqd(32, [1, 10, 25]))
