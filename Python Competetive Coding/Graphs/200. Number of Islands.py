class Solution(object):
    def numIslands(self, grid):
        """:type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        def sink_island(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            
            sink_island(r-1, c)
            sink_island(r+1, c)
            sink_island(r, c-1)
            sink_island(r, c+1)

        for r in range(0, rows):
            for c in range(0, cols):
                if grid[r][c] == '1':
                    island_count += 1
                    sink_island(r, c)
        return island_count

sol = Solution()
input = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(sol.numIslands(input))  # Output will now correctly be 1