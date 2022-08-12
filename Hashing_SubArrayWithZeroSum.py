def isZeroSum(array) -> bool:
    prefixSum = 0
    hashSet = set()
    for i in range(len(array)):
        prefixSum += array[i]
        if prefixSum == 0 or prefixSum in hashSet:
            return True
        hashSet.add(prefixSum)
    return False


print(isZeroSum([-3, 4, -3, -1, -1, 4, 5]))
print(isZeroSum([-3, 10, -3, -2, -1, 4, 5]))
