# NEETCODE Best Solution:
# Our goal in this question is to build an algorithm to guess the `pick` most efficiently- so that algo would run in O(logn) time- BINARY SEARCH.

# Here, we are given a `guess` API which returns
# -1: Your guess is higher than the number I picked --> go towards left
# 1: Your guess is lower than the number I picked --> go towards right
# 0: your guess is equal to the number I picked

# So we run a loop till we guess the correct number, and implement Binary Search algorithm, and update l and r pointers according to what result we get out of -1, 1 or 0. 
# Assign the result to a variables `res` and compare res with 0

# TC = O(logn)
# SC = O(1)

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        l, r = 0, n

        while True:
            m = (l + r) // 2
            res = guess(m)

            if res < 0:
                r = m - 1
            elif res > 0: 
                l = m + 1
            else:
                return m

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
