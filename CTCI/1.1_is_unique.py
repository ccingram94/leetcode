
# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters.  
# Solution: Because a set's elements are unique, compare the given string to its set counterpart.

def isUnique(string):
    if string == set(string):
        return True
    else:
        return False