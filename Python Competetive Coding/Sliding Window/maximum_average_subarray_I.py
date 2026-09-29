"""643. Maximum Average Subarray I
Easy
Topics
premium lock icon
Companies
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) < k:
            return 0.00000
        sum = 0
        for i in range(0, k):
            sum += nums[i]
        average_sum = float(sum)/k
        left = 0
        right = k
        while right < len(nums):
            sum = sum - nums[left] + nums[right]
            ave = float(sum)/k
            average_sum = max(average_sum, ave)
            left += 1
            right += 1
        return average_sum

nums = [1,12,-5,-6,50,3]
k = 4
sol = Solution()
print(sol.findMaxAverage(nums, k))