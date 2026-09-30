"""
20. Valid Parentheses
Easy
Topics
premium lock icon
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1 :
            return False
        stack = []
        ele_map = {
            ')' : '(',
            '}' : '{',
            ']' : '[' 
        }
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                expected_opening_bracket = ele_map[s[i]]
                ele_pop = stack.pop()
                if ele_pop != expected_opening_bracket:
                    return False
        return True if len(stack) == 0 else False
s= "(("
sol = Solution()
print(sol.isValid(s))