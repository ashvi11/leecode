# Approach 1: Keep dividing number by for each item i in list, keep dividing the element by 10 until it's no longer divisible, and simultaneously, keep incrementing the 
# 'div' counter(number of times it got divided by 10). If 'div' is even, increment 'count' counter. Reset 'div' counter and follow these steps for other elements. 
# Return the 'count' counter.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        div = 0
        count = 0
        for i in nums:
            while i != 0:
                i = i//10
                div += 1
            if div % 2 == 0:
                count += 1 
            div = 0
        return count
                    
 
# Approach 2: For each element in the list, check the length of 'string' of each element. If it is divisible by 2, increment counter. Return counter.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count
                
