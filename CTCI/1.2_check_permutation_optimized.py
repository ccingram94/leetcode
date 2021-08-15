
# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
# Solution: use a dictionary to keep track of the already present characters in the strings

def checkPermutation(string1, string2):
    if len(string1) != len(string2):
        return False

    count = {} # initialize a dictionary

    for i in string1: #for each character in string1
        count[i] = count.get(i, 0) + 1 # if character not in dictionary, add character as key with value of 1

    for i in string2: #for each character in string2
        if i in count: #if character in dictionary "count"
            count[i] -= 1 #decrement the value of that character's key
            if count[i] == 0: #if that key value now zero
                del count[i] #delete that key/value pair
        else:
            return False #if character not in dictionary, they must not be permutations
    
    return len(count) == 0 #if strings are permutations, count dictionary should not be empty

# time complexity: O(n)
# space complexity: O(n)