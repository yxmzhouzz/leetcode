# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
#


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTri = []
        pascalTri.append([1])
        pascalTri.append([1, 1])
        if numRows > 2:
            for i in range(2, numRows):
                temp = [1]
                temp.extend([pascalTri[i-1][j] + pascalTri[i-1][j+1] for j in range(i-1)])
                temp.append(1)
                pascalTri.append(temp)
        return pascalTri[: numRows]
