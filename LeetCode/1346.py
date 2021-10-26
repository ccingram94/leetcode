# 1346. Check If N and Its Double Exist -- Given an array "arr" of integers, check if there exist two integers N and M such that N is the double of M.
# Solution: Create a hashmap to store each element, then compare possible answers to existing values in the hashmap.  (Return answer as Boolean)

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashmap = {}
        for m in range(len(arr)):
            if arr[m]*2 in hashmap:
                return True
            if arr[m]/2 in hashmap:
                return True
            hashmap[arr[m]] = m
                
        

# leetcode results:
# success
# Runtime: 40 ms, faster than 99.51% of Python3 online submissions for Check If N and Its Double Exist.
# Memory Usage: 14.4 MB, less than 17.79% of Python3 online submissions for Check If N and Its Double Exist.
