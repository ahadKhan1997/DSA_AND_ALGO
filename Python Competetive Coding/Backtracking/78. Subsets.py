"""
https://leetcode.com/problems/subsets/description/

78. Subsets
Medium
Topics
premium lock icon
Companies
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        current_subset = []
        
        def backtrack(index):
            result.append(list(current_subset))
            
            for i in range(index, len(nums)):
                current_subset.append(nums[i])
                
                backtrack(i + 1)
                
                current_subset.pop()
                
        backtrack(0)
        return result
