# Approach 1:
# We'll keep subctracting 1 to n from n. 
# Eg: n = 17
# 17 - 1 = 16- row 1 complete- still have 16 coins left
# 16 - 2 = 14- row 2 complete- still have 14 coins left
# 14 - 3 = 11- row 3 complete- still have 11 coins left
# 11 - 4 = 7- row 4 complete- still have 7 coins left
# 7 - 5 = 2- row 5 complete- still have 2 coins left
# 2 - 6 = -4 < 0- row 6 cannot be completed- don't have enough coins(ans is negative- only 2 coins left as per above)
# This way, we'll stop the loop when ans is negative
# But we are incrementing counter anyway after calculating the diff- counter will stop when the next time loop will break
# So we return counter - 1
# When n = 1- it's a special case, so we write an edge case for it

# Time Complexity = O(n)
# Space Complexity = O(1)

class Solution:
    def arrangeCoins(self, n: int) -> int:

        diff = n
        i = 1
        count = 0

        while i <= n and diff >= 0:
            diff = diff - i
            count += 1
            i += 1
        
        return count - 1 if n != 1 else 1

-----------------------------------------------------------------------------------------------------------------------------------------

# NEETCODE Best Solution: BINARY SEARCH
# We know we have a formula to calculate sum of A.P.- 1 + 2 + 3 + 4 + ... + r = n
# r(r + 1)/2 = n
# so we'll have to SEARCH for r in the bound 1 to n, because we are given in the question that 
# there will be at least 1 coin, and we'll have at most n rows for n coins.
# So write a Binary Search algorithm- when n == m(m+1)/2, then it means we have found rows in which we have fit n coins, so return m
# when n < m(m+1)/2, then it means that that row(m) needs more coins than we actually have, so m or any number > m will be eliminate
# when n > m(m+1)/2, then it means that that row(m) needs less coins than we actually have, so m could be a candidate for our answer.
# we need highest candidate that is < n. Return the highest candidate.

# Time Complexity = O(logn)
# Space Complexity = O(1)

class Solution:
    def arrangeCoins(self, n: int) -> int:

        # 1 + 2 + 3 + 4 + ... + x = n
        # x(x+1)/2 = n
        # so x will be our number of rows that sums up to n

        l, r = 0, n
        res = 1

        while l <= r:
            m = (l + r) // 2
            coins = m*(m+1)/2

            if coins == n:
                return m
            if coins > n:
                r = m - 1
            else:
                l = m + 1
                res = m
        return res
            
-----------------------------------------------------------------------------------------------------------------------------------------

# Math Approach:

# Another approach is to take the equation r(r+1)/2, and solve for r
# According to Neetcode, it will take O(1) time, but in reality, when we solve for r^2 + r - 2n = 0, we are solving 
# a quadratic equation. So we'll need to use sqrt() at some point. 
# TC of sqrt() is root(n)
# I tried coding this solution but it doesn't work. Maybe Ayush can help
