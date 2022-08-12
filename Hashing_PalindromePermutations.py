from collections import Counter


def isPalindromePermutations(string) -> bool:
    countFrequency = Counter(string)
    oddFrequency = 0
    for freq in countFrequency.values():
        if freq % 2 != 0:
            oddFrequency += 1
            if oddFrequency > 1:
                return False
    return True


print(isPalindromePermutations("abcc"))
print(isPalindromePermutations("acbccab"))
