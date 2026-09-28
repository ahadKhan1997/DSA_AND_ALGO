# 1. Two Sum
# Easy
# Hint
# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


class Solution(object):

    def __init__(self, nums, target):
        # Call the twoSum function using self and print or store the result
        self.result = self.twoSum(nums, target)
        print(f"Result found inside __init__: {self.result}")
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """res = []
        j = 0
        i = 1
        while i < len(nums):
            if nums[i] + nums[j] == target:
                res = [j, i]
                return res
            
            # Reset mechanics work perfectly here
            if i == len(nums) - 1 and j < len(nums) - 1:
                j = j + 1
                i = j + 1
            else:
                i = i + 1  # Standard step forward
                
        return res"""

        # optimized version
        seen = {}
        
        for i, num in enumerate(nums):
            # Calculate what number we need to reach the target
            complement = target - num
            
            # If we have already seen that required number, we found our pair!
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, save the current number and its index to the dictionary
            seen[num] = i
                
        return []

example_nums = [3,2,4]
example_target = 6

sol = Solution(example_nums, example_target)

    
