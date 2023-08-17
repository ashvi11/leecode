# Approach 1: BRUTE FORCE- DOESN'T WORK IN LC- time limit exceeds

# Check all numbers from 0 to num. If i*i == num, it means we've reached a number whose square = num, so return True
# Else, return False

# TC = O(n) because loop will only run n times
# SC = O(1)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        for i in range(1, num+1):
            if i*i == num:
                return True
        return False

-----------------------------------------------------------------------------------------------------------------------------------------

# Approach 2: 

# Check all numbers from 0 to num. If i*i == num, it means we've reached a number whose square = num, so return True
# But if i*i > num, it means we are at a number whose square is > num, and there is no point in checking futher because 
# all squares from now on will be > num, so return False

# TC = O(sqrt(n)) because loop will only run n times
# SC = O(1)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        for i in range(1, num+1):
            if i*i == num:
                return True
            elif i*i > num:
                return False
        return

-----------------------------------------------------------------------------------------------------------------------------------------

# NEETCODE Best Solution: BINARY SEARCH

# Check from 0 to num using Binary Search. Use l, r and m pointers- keep updating these pointers according to binary search algorithm. 
# When m^2 == num, we can say num is square of m, and return True. 
# But if m^2 > num, then the number is too large, and we need to search the left part of the remaining array. 
# When m^2 < num, then the number is too small, and search right part of the remaining array. 
# At some point, if num is a perfect square, it's square root will be encountered as m, and True will be returned. 
# If True is not returned at all, return False.

# TC = O(logn)
# SC = O(1)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        l, r = 1, num

        while l <= r:
            m = (l + r) // 2
            if m*m == num:
                return True
            elif m*m > num:
                r = m - 1
            else:
                l = m + 1
              
        return False

-----------------------------------------------------------------------------------------------------------------------------------------

