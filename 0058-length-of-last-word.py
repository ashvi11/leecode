# NEETCODE Best Solution:
# Start from the end of the string. If spaces are encountered, ignore and move forward. When the letter is encountered for the first time, increment the counter. Keep incrementing the counter till 
# a space is encountered. 
# Return counter

# TC = O(n) ~ len(s)
# SC = O(1)- we created only 1 variable, so O(1)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        length, i = 0, len(s)-1
        count = 0

        while s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1
        
        return count

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Approach 2-
# Another approach would be to split the string into words, and then return the length of last word- it might not be allowed in the interview because it's a Python cheat and too easy

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        split_s = s.split()

        return len(split_s[-1])
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
