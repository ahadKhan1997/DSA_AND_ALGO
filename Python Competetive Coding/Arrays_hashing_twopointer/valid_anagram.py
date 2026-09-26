"""
242. Valid Anagram
Solved
Easy


Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
from collections import Counter
class Solution(object):
    def __init__(self, s, t):
        # Call the twoSum function using self and print or store the result
        self.result = self.isAnagram(s, t)
        print(f"Result found inside __init__: {self.result}")

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        # s = "".join(sorted(s))
        # t = "".join(sorted(t))
        # if(t == s):
        #     return True
        # return False
        return Counter(s) == Counter(t)
    
t = "tan"
s = "nar"
sol = Solution(s, t)