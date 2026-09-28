"""
125. Valid Palindrome
Easy
Topics
premium lock icon
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

import re

class Solution(object):
    def __init__(self, s):
        # Call the twoSum function using self and print or store the result
        self.result = self.isPalindrome(s)
        print(f"Result found inside __init__: {self.result}")

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if len(s) == 0 or len(s) == 1:
            return True
        i = 0
        j = len(s) - 1

        while i != j and i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
s = "a"
sol = Solution(s)