"""
42. Trapping Rain Water
Hard
Topics
premium lock icon
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        max = 0
        left_max = height[0]
        right_max = height[len(height)-1]
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] > left_max:
                left_max = height[left]
            if height[right] > right_max:
                right_max = height[right]
            if(left_max < right_max):
                max += left_max - height[left]
                left += 1
            else:
                max += right_max - height[right]
                right -= 1
        return max
sol = Solution()
height = [0, 0, 5, 0, 0]
print(sol.trap(height))

            
            
