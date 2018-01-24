class Solution(object):
    def maxAreaOfIsland(self, grid):
        # m, n = len(grid), len(grid[0])
        # def dfs(i, j):
        #     if 0 <= i < m and 0 <= j < n and grid[i][j]:
        #         grid[i][j] = 0
        #         return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
        #     return 0
        # areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        # return max(areas) if areas else 0

        def dfs(new_i, new_j, new_grid):
            if 0 <= new_i < m and 0 <= new_j < n and new_grid[new_i][new_j]:
                new_grid[new_i][new_j] = 0
                temp = 1 + dfs(new_i + 1, new_j, new_grid) + dfs(new_i, new_j + 1, new_grid) + dfs(new_i - 1, new_j,new_grid) + dfs(new_i, new_j - 1, new_grid)
                new_grid[new_i][new_j] = 1
                return temp
            return 0

        max_area = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if (grid[i][j]):
                    temp_area = dfs(i, j, grid)
                    if (max_area < temp_area):
                        max_area = temp_area
        return max_area
########################### Optimized discussio solution #############

        # m, n = len(grid), len(grid[0])
        # def dfs(i, j):
        #     if 0 <= i < m and 0 <= j < n and grid[i][j]:
        #         grid[i][j] = 0
        #         return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
        #     return 0
        # areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        # return max(areas) if areas else 0
temp=Solution()
grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],
      [0,0,0,0,0,0,0,1,1,1,0,0,0],
      [0,1,1,0,1,0,0,0,0,0,0,0,0],
      [0,1,0,0,1,1,0,0,1,0,1,0,0],
      [0,1,0,0,1,1,0,0,1,1,1,0,0],
      [0,0,0,0,0,0,0,0,0,0,1,0,0],
      [0,0,0,0,0,0,0,1,1,1,0,0,0],
      [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(temp.maxAreaOfIsland(grid))