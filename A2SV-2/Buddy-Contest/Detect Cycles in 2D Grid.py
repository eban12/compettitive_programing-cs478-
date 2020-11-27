class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited:
                    if self.dfs(grid, (i,j), (-1,-1), grid[i][j], visited):
                        return True
        return False
    
    def dfs(self, grid, current, prev, curChar, visited):
        if current in visited:
            return True
        
        visited.add(current)
        for i, j in [(current[0]+1, current[1]), (current[0]-1, current[1]), (current[0], current[1]+1), (current[0], current[1]-1)]:
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i,j) != prev and grid[i][j] == curChar:
                if self.dfs(grid, (i,j), current, curChar, visited):
                    return True
