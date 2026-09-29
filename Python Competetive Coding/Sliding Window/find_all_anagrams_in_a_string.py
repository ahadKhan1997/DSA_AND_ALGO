"""
438. Find All Anagrams in a String
Medium
Topics
premium lock icon
Companies
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        arr = []
        if len(s) < len(p):
            return arr
            
        p_dict = {}
        s_dict = {}
        for i in range(len(p)):
            p_dict[p[i]] = p_dict.get(p[i], 0) + 1
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            
        left = 0
        if s_dict == p_dict:
            arr.append(left)
            
        # Slide the window across the rest of string s
        for right in range(len(p), len(s)):
            # 1. Add the incoming character on the right
            s_dict[s[right]] = s_dict.get(s[right], 0) + 1
            
            # 2. Remove/Decrement the outgoing character on the left
            s_dict[s[left]] -= 1
            if s_dict[s[left]] == 0:
                del s_dict[s[left]] # Direct deletion without a loop!
                
            left += 1
            
            # 3. Compare the profiles
            if s_dict == p_dict:
                arr.append(left)
                
        return arr
s = "abab"
p = "abc"
sol = Solution()
print(sol.findAnagrams(s, p))
