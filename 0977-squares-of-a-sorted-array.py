# NEETCODE Best Solution:

# We'll create 2 pointers- at the start and at the end of the array. 
# Now since 0 will always be the smallest square if it's present in the array, numbers on right of 0 and left of 0 will have squares > 0. 
# So we cannot determine the smallest one.
# So we'll determine the largest, keep appending the larger one in the array, and return the reversed array.

# Time Complexity = O(n) ~ (n + n)- one pass +  reversing array
# Space Complexity = O(1)- res array is not considered extra space

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        res = []
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[r] * nums[r] > nums[l] * nums[l]:
                res.append(nums[r] * nums[r])
                r -= 1
            else:
                res.append(nums[l] * nums[l])
                l += 1
        return res[::-1]

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# NEETCODE Best Solution:

# This solution is same as the previous one, but instead of appending the largest element in the array, and reversing the array, 
# we just push the largest to smallest element from the end to start of the array.

# Time Complexity = O(n)- one pass
# Space Complexity = O(1)- res array is not considered extra space

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        l, r = 0, n-1
        res = [0] * n

        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                res[(r - l)] = nums[l] * nums[l]
                l += 1
            else:
                res[(r - l)] = nums[r] * nums[r]
                r -= 1
        
        return res

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

