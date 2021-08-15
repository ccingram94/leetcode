
# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
# Solution: If they are permutations of each other, the sorted strings should be equal.

def checkPermutation(string1, string2):
    if len(string1) != len(string2):
        return False
    string1 = sorted(string1)
    string2 = sorted(string2)
    return (string1 == string2)

# time complexity: O(n log n) to sort the strings
# space complexity: 0(n) for the newly sorted strings