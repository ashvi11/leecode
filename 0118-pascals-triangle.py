# NEETCODE Best Solution:

# The trick is to add zeros as the first and last elements of each row.
# First create the first row manually. We will use this to derived other rows
# Then create a for loop in the range numRows-1 because we already created the first row, so now we only need to derived numRows-1 rows
# in this loop, create a temp array- pick the last most element(row) of already derived rows. Add 0 at the first position and at the last position
# now we need to add 2 elements at a time of this temp array, so again create a for loop from 0 to len(temp)-1 because if we do len(temp) then we'll have index out of bound error on last summation.
# keep appending these summation values to a new array
# finally append this new array(row) to the main result. Return Result


# Time Complexity = O(n^2)
# Space Complexity = O(n^2)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:


        res = [[1]]

        for i in range(numRows-1):
            temp = [0] + res[-1] + [0]

            new = []
            for j in range(len(temp)-1):
                new.append(temp[j] + temp[j+1])
            
            res.append(new)
        
        return res
      

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
