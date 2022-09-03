# Approach 1: Logic- Keep updating count whenever we get 1, reset the counter otherwise
# Code: Create a variable count and maxcount. Start a for loop. If 1 is encountered, keep incrementing the count. Keep updating maxcount. If 0 is encountered, 
# reset the count variable. In the end, return the maxcount.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxcount = 0
        for i in nums:
            if i == 1:
                count += 1
                maxcount = max(count, maxcount)
   
            else:
                count = 0
        return maxcount
    
    
