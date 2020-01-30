class Solution:
    def minimumMoves(self, grid) -> int:
        n = len(grid)
        hMoves = [[float('inf')] * (n + 1) for i in range(n + 1)]
        vMoves = [[float('inf')] * (n + 1) for i in range(n + 1)]
        hMoves[1][1] = 0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if grid[i-1][j-1] == 1:
                    continue
                
                if j < n and grid[i-1][j] == 0:
                    hMoves[i][j] = min(hMoves[i][j], hMoves[i][j-1]+1, hMoves[i-1][j]+1)
                
                if i < n and grid[i][j-1] == 0:
                    vMoves[i][j] = min(vMoves[i][j], vMoves[i][j-1]+1, vMoves[i-1][j]+1)

                if hMoves[i][j] + 1 < vMoves[i][j] and i<n and grid[i][j-1] == 0 and grid[i][j] == 0:
                    vMoves[i][j] = hMoves[i][j] + 1
                
                if vMoves[i][j] + 1 < hMoves[i][j] and j<n and grid[i-1][j] == 0 and grid[i][j] == 0:
                    hMoves[i][j] = vMoves[i][j] + 1
        
        if hMoves[-1][-2] == float('inf'):
            return -1
        
        return hMoves[-1][-2]
