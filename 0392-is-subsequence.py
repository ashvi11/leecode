# NEETCODE Best Solution:
# Use two-pointer approach- initiate pointer i at first position of s, pointer j at first position of t. If s[i] != t[j], keep incrementing j, if both are equal, increment both pointers.
# At the end, if i = out of bounds of s, we conclude that s is subsequence of t, else it's not.

# Time Complexity = O(n) ~ O(s + t) because we are possible iterating over all elements of s and t once
# Space Complexity = O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return True if i == len(s) else False
      
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
