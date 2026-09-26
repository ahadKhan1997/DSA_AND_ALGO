""""
49. Group Anagrams
Medium
Topics
premium lock icon
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 1:
            return[[strs[0]]]
        obj = {}
        for str in strs:
            sorted_txt = "".join(sorted(str))
            if sorted_txt in obj:
                tempArr = obj[sorted_txt]
                tempArr.append(str)
                obj[sorted_txt] = tempArr
            else:
                obj[sorted_txt] = [str]
        res = []
        for val in obj.values():
            res.append(val)
        return res

strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
res = sol.groupAnagrams(strs)
print(res)
res = sol.groupAnagrams([""])
print(res)
        