class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        closed = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    if self.helper(grid, (i, j)):
                        closed += 1
        return closed
    
    def helper(self, grid, origin):
        directions = [(-1,0), (0,-1), (1,0), (0,1)]
        stack = []
        stack.append(origin)
        flag = True
        while stack:
            temp = stack.pop()
            for i in directions:
                r, c = i
                r += temp[0]
                c += temp[1]
                if (not (0 <= r < len(grid))) or not (0 <= c < len(grid[0])):
                    flag = False
                elif (0 <= r < len(grid)) and (0 <= c < len(grid[0])) and grid[r][c] == 0:
                    stack.append((r,c))
                    grid[r][c] = -1
                
        return flag
