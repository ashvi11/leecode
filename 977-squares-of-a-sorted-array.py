#Approach 1- Calculate squares of all elements, and create a new empty array. Make two pointers, left L and right R. Compare these squares at index L and R, 'append' the 
# higher number in the new array. This will make the new array sorted in descending order. Reverse the array and return it.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            nums[i] = nums[i] * nums[i]
        sqr = []
       
        l = 0
        r = len(nums)-1
        
        while l <= r:
            if nums[l] < nums[r]:
                sqr.append(nums[r])
                r-=1
            else:
                sqr.append(nums[l])
                l+=1
    
        return sqr[::-1]
        
# TC = O(n) (for loop- n, while loop- n, reversing the list- n = (n+n+n) = 3n ~ n)
# SC = O(n) (created a new array)

# Approach 2- NEETCODE- Same as 1, but instead of squaring the elements before, we square at the time of appending.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left = 0
        right = len(nums) - 1
        sqrs_lst = [] 
        
        while left <= right:
            
            if nums[left]**2 > nums[right]**2:
                sqrs_lst.append(nums[left]**2)
                left += 1
            else:
                sqrs_lst.append(nums[right]**2)
                right -= 1
            
        return sqrs_lst[::-1]
        
# TC = O(n) (for loop- n, while loop- n, reversing the list- n = (n+n+n) = 3n ~ n)
# SC = O(n) (created a new array)

# Approach 3- LEETCODE SOLUTIONS- Same as approach 2, but instead of 'inserting elements in an array', we create an array of length 'n' and edit it's elements. Here in for loop, we are 
# going from right to left instead of left to right, so we were not reversing the list at the end.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        r = n-1
        lis = [0] * n

        for i in range(n-1, 0, -1):
            if abs(nums[l]) < abs(nums[r]):
                sqr = nums[r] * nums[r]
                r-=1
            else:
                sqr = nums[l] * nums[l]
                l+=1
            lis[i] = sqr

        return lis
    
# TC = O(n) (for loop- n)
# SC = O(n) (created a new array)


                
