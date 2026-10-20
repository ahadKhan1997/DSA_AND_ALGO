"""
https://leetcode.com/problems/word-search/description/

79. Word Search
Medium
Topics
premium lock icon
Companies
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, index, board):
            if index == len(word):
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[index]:
                return False

            temp = board[r][c]
            board[r][c] = '#'

            found = (dfs(r-1, c, index + 1, board) or
                     dfs(r, c-1, index + 1, board) or
                     dfs(r+1, c, index + 1, board) or
                     dfs(r, c+1, index + 1, board))

            board = temp
            return found
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0, board):
                    return True
        return False

sol = Solution()
word = "ABCCEA"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(sol.exist(board, word))