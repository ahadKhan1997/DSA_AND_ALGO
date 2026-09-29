"""
424. Longest Repeating Character Replacement
Medium
Topics
premium lock icon
Companies
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        char_map = {}
        max_count = 0
        max_length = 0
        
        for right in range(len(s)):
            # Clean way to increment count without if/else
            char_map[s[right]] = char_map.get(s[right], 0) + 1
            max_count = max(max_count, char_map[s[right]])
            
            # Changing 'while' to 'if' works perfectly here
            if (right - left + 1) - max_count > k:
                char_map[s[left]] -= 1
                left += 1
                
            max_length = max(max_length, right - left + 1)
            
        return max_length
s = "ABCD"
k = 1
sol = Solution()
print(sol.characterReplacement(s, k))



            