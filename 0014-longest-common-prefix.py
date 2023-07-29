# NEETCODE Best Solution:

# Pick the first string from the list, now we'll compare all strings against this string including itself. Comare each index of this string to same index of other strings. 
# If they are not equal, return result uptil that point. If matches and add that element to the result.

#Handling edge case- first string we picked for comparision might not be the shortest, so we need to handle that. Eg. length of that string = 6, length of string after that is 4, so loop will throw 
# out of index error after 4 times. To handle this, see if that index == len(later string). If so, return res. 
# Python checks an or loop- if the first condition is True, Python returns True and does not check second condition.

# Time Complexity = O(m.n)- m =  number of strings, n = len of shortest string
# Space Complexity = O(n)- n = len of shortest stringecause the shortest string can be prefix, prefix cannot be longer than the shortest string. 
# Also, strings are immutable, so each time a new res is created. eg. O(1) + O(2) + O(3) + O(4)...+ O(n), so we consider O(n) to be the highest degree

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ''

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return res
            res += strs[0][i]
        return res

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
