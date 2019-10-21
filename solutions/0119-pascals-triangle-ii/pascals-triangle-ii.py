# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
#
# Note that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
#
# Input: 3
# Output: [1,3,3,1]
#
#
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?
#


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        # exceed time limit
        if rowIndex == 0:
            temp = [1]
        if rowIndex == 1:
            temp = [1, 1]
        if rowIndex >= 2:
            temp = [1]
            temp.extend([self.getRow(rowIndex-1)[i] + self.getRow(rowIndex-1)[i+1] for i in range(rowIndex-1)])
            temp.append(1)
        return temp
        """
        
        # store every line in the triangle to avoid recalculate the getRow function
        p = []
        p.append([1])
        p.append([1,1])
        if rowIndex>=2:
            for i in range(2, rowIndex+1):
                temp = [1]
                temp.extend([p[i-1][j]+p[i-1][j+1] for j in range(i-1)])
                temp.append(1)
                p.append(temp)
        return p[rowIndex]
