import time

def almost_all(numbers):
    """ """
    result = []
    sums = sum(numbers)
    for i in range(len(numbers)):
        result.append(sums - numbers[i])
    return result

almost_all(list(range(10**5)))
print("OK")
print(almost_all([1,2,3]))