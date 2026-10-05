"""
https://leetcode.com/problems/search-a-2d-matrix/description/

74. Search a 2D Matrix
Medium
Topics
premium lock icon
Companies
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        lm = 0
        rm = len(matrix) - 1
        while lm <= rm:
            mm = int((lm + rm)/2)
            mid_array = matrix[mm]
            ln = 0
            rn = len(mid_array) - 1
            found = None
            while ln <= rn:
                mn = (ln +rn)//2
                if mid_array[mn] == target:
                    return True
                elif mid_array[mn] > target:
                    found = "smaller"
                    rn = mn - 1
                else:
                    found = "greater"
                    ln = mn + 1
            if found == "smaller":
                rm = mm - 1
            else:
                lm = mm + 1
        return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 16
sol = Solution()
print(sol.searchMatrix(matrix, target))