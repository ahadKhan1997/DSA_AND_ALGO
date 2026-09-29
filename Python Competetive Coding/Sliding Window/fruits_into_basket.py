"""
904. Fruit Into Baskets
Medium
Topics
premium lock icon
Companies
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length

"""


class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        k = 2
        left = 0
        max_trees = 0
        fruit_map = {}
        for right in range(0, len(fruits)):
            fruit_map[fruits[right]] = fruit_map.get(fruits[right], 0) + 1
            if len(fruit_map) > k:
                fruit_map[fruits[left]] -= 1
                if fruit_map[fruits[left]] == 0:
                    del fruit_map[fruits[left]]
                left += 1
            max_trees = max(max_trees, right-left+1)
        return max_trees
fruits = [1,2,3,2,2,2,3,3,3,4,5,5,5,5,5,5]
sol = Solution()
print(sol.totalFruit(fruits))