""""
347. Top K Frequent Elements
Medium
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums
        obj = {}
        for num in nums:
            if num in obj:
                obj[num] = obj[num] + 1
            else:
                obj[num] = 1
        arr = []
        sorted_obj = sorted(obj, key = obj.get, reverse=True)
        i = 0
        for key in sorted_obj:
            if i == k:
                break
            arr.append(key)
            i += 1
        return arr
nums = [3,0,1,0]
k = 1
sol = Solution()
res = sol.topKFrequent(nums, k)
print(res)