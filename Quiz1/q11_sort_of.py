def sort_of(numbers): 
    result = [] 
    if len(numbers) == 0:
        return result
    else:
        mini = numbers[-1]
        for i in range(len(numbers)-1, -1, -1):  
            if numbers[i] < mini:
                result.append(numbers[i])
                mini = numbers[i]
            else:
                result.append(mini)
        result.reverse()
        return result        


print(sort_of([1, 2, 3, 3]))
print(sort_of([3, 3, 2, 1]))
print(sort_of([1, 2, 3, 2, 4, 5]))
print(sort_of([]))
sort_of(list(range(10**5)))
print("OK")