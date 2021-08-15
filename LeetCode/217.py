# 217. Contains Duplicate -- Given an integer array "nums", return "true" if any value appears at least twice in the array, and return "false" if every element is distinct.
# Solution: Because a set is made of unique values, compare the given array to its set counterpart to determine if there are duplicates.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True

# leetcode results:
# success
# runtime: Runtime: 116 ms, faster than 78.84% of Python3 online submissions for Contains Duplicate.
# memory usage: Memory Usage: 20.1 MB, less than 38.06% of Python3 online submissions for Contains Duplicate.
