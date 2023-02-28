# when nums[i] not equal to val, update the value of nums[k] to nums[i], then move k 1 index right. i will move right in any case



class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      k = 0
      for i in range(len(nums)):
        if nums[i] != val:
          nums[k] = nums[i]
          k += 1
      return k
    
# TC = O(n) (for loop- n)
# SC = O(1) (inplace)


