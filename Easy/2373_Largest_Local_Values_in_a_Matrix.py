class Solution(object):
    def largestLocal(self, grid):
        N = len(grid)
        ans = [[0] * (N - 2) for _ in range(N - 2)]

        for i in range(N - 2):
            for j in range(N - 2):
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        ans[i][j] = max(ans[i][j], grid[k][l])
        return ans 
        