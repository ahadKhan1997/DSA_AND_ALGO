"""
76. Minimum Window Substring
Hard
Topics
premium lock icon
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

class Solution(object):
    def minWindow(self, s, t):
        if not s or not t or len(s) < len(t):
            return ""

        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        s_dict = {}
        
        have, need = 0, len(t_dict)
        
        min_len = float("inf")
        res_indices = [-1, -1]
        
        l = 0
        for r in range(len(s)):
            char = s[r]
            s_dict[char] = s_dict.get(char, 0) + 1
            
            if char in t_dict and s_dict[char] == t_dict[char]:
                have += 1
                
            while have == need:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    res_indices = [l, r]
                    
                left_char = s[l]
                s_dict[left_char] -= 1
                
                if left_char in t_dict and s_dict[left_char] < t_dict[left_char]:
                    have -= 1
                    
                l += 1
                
        l, r = res_indices
        return s[l : r + 1] if min_len != float("inf") else ""

s = "ADOBECODEBANC"
t = "ABC"
sol = Solution()
print(sol.minWindow(s, t))