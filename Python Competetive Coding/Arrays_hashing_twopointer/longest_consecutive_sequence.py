"""
128. Longest Consecutive Sequence
Medium
Topics
premium lock icon
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        # sorted_nums = sorted(nums)
        # res = 1
        # temp_counter = 1
        # i = 0
        # while i < len(sorted_nums):
            
        #     while i < len(sorted_nums) - 1 and sorted_nums[i] == sorted_nums[i + 1]:
        #         i += 1
        #     if i < len(sorted_nums) - 1 and sorted_nums[i] + 1 == sorted_nums[i + 1] :
        #         temp_counter += 1
        #     else:
        #         temp_counter = 1
        #     if temp_counter > res:
        #         res = temp_counter
        #     i += 1
        # return res

        # optimised
        set_nums = set(nums)
        longest_streak = 0
        for num in set_nums:
            if num - 1 not in set_nums:
                current = num
                streak = 1

                while current + 1 in set_nums:
                    current += 1
                    streak += 1
                if streak > longest_streak:
                    longest_streak = streak
        return longest_streak
sol = Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
print(sol.longestConsecutive(nums))