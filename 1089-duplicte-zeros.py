# whenever we encounter a '0', we 'pop' an element(delete from the end of array), and 'insert' 0 at the current location. Skip 2 indexes, and go to next 
# index. Do this until i < len(arr). If we encounter 1, go to next index.

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.pop()
                arr.insert(i, 0)
                i += 2
            else:
                i += 1

                
# TC = O(n^2) (while loop- n, insert operation- n, hence n*n = n^2)
# SC = O(1)
