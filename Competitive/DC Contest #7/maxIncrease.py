class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        skylineBU = []
        skylineRL = []
        for i in range(len(grid)):
            skylineRL.append(max(grid[i]))
        
        
        cols = [[] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cols[j].append(grid[i][j])
                
        for i in range(len(cols)):
            skylineBU.append(max(cols[i]))
        
        maxSum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxSum += min(skylineRL[i], skylineBU[j]) - grid[i][j]
        
        return maxSum
                
