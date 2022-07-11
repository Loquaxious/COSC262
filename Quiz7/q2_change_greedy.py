from collections import defaultdict

def change_greedy(amount, coinage):
    """Takes an integer amount of money in some units plus a list of
    coin values an returns the breakdown of that amount into coins as 
    obtained by the greedy algorithm"""
    
    n = len(coinage)
    sort_coins = sorted(coinage)
    sort_coins.reverse()
    counts = defaultdict(int) # counters of all coins
    i = 0
    breakdown = []
    
    try:
        while (amount > 0):
            while sort_coins[i] <= amount:
                counts[sort_coins[i]] +=1
                amount -= sort_coins[i]
            i += 1
    except:
        return None
    
    for key, count in counts.items():
        breakdown.append((count, key))
    return breakdown


print(change_greedy(82, [1, 10, 25, 5]))
print(change_greedy(80, [1, 10, 25]))
print(change_greedy(82, [10, 25, 5]))    
    