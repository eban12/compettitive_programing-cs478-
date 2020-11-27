class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j].isupper():
                    if self.dfs(grid, (i,j), (-1,-1), grid[i][j]):
                        return True
        return False
    
    def dfs(self, grid, cur, prev, curChar):
        x, y = cur
        if grid[x][y].isupper():
            return True
        
        grid[x][y] = grid[x][y].upper()
        for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i,j) != prev and grid[i][j].lower() == curChar:
                if self.dfs(grid, (i,j), cur, curChar):
                    return True
