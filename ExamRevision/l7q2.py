from collections import defaultdict

def change_greedy(amount, change):
    counts = defaultdict(int)
    change.sort(reverse=True)
    while amount > 0:
        for i in range(len(change)):
            if amount - change[i] >= 0:
                amount -= change[i]
                counts[change[i]] += 1
                break
            elif i == len(change) - 1:
                return None 
    
    breakdown = []
    for key, value in counts.items():
        breakdown.append((value, key))
    return breakdown

print(change_greedy(82, [1, 10, 25, 5]))
print(change_greedy(80, [1, 10, 25]))
print(change_greedy(82, [10, 25, 5]))
