# NEETCODE Optimal Solution:
# Check from 0 to x using Binary Search. Use l, r and m pointers- keep updating these pointers according to binary search algorithm. 
# When m^2 == x, we can say x is square of m, and return m. But if m^2 > x, then the number is too large, 
# and we need to search the left part of the remaining array. 
# When m^2 < x, it means that m is one of the candidates(because the question asks us to round down), 
# and of all those candidates, we need the highest value candidate because it will be the closest square root of x. 
# Return highest candidate.

# Time Complexity = O(logn)
# Space Complexity = O(1)

class Solution:
    def mySqrt(self, x: int) -> int:

        l, r = 0, x
        max_res = 0
        res = 0

        while l <= r:
            m = (l + r) // 2
            if m*m == x:
                return m
            elif m*m > x:
                r = m - 1
            else:
                res = m
                max_res = max(max_res, res)
                l = m + 1
        return max_res

----------------------------------------------------------------------------------------------------------------------------------------

# NEETCODE Optimal Solution:
# Implement binary search as above.
# Our current m is the highest at that point. If we are going to move right, and next m is on the right of curr m, 
# then new m is greater candidate.
# This code simplifies the solution by returning just the highest candidate without using max().

# Time Complexity = O(logn)
# Space Complexity = O(1)

class Solution:
    def mySqrt(self, x: int) -> int:

        l, r = 0, x
        res = 0

        while l <= r:
            m = (l + r) // 2

            if m*m == x:
                return m
            elif m*m > x:
                r = m - 1
            else:
                l = m + 1
                res = m
        return res

----------------------------------------------------------------------------------------------------------------------------------------


        
