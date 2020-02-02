class Solution:
    def largestIsland(self, grid):
        islands = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    size, border = self.findIslandSize(grid,(i,j))
                    islands.append([size,border])
        if not islands:
            return 1
        
        maxIsland = 0
        maxSize = 0
        for i in range(len(islands)):
            m = islands[i][0]
            intersection = set()
            for j in range(len(islands)):
                if i != j and (islands[i][1] & islands[j][1]):
                    if intersection & islands[j][1]:
                        size += islands[j][0]
                        intersection = intersection & islands[j][1]
                    else:
                        size = islands[i][0] + islands[j][0]
                        intersection = islands[i][1] & islands[j][1]
                    if size > m:
                        m = size
            
            if m > maxSize:
                maxSize = m
                maxIsland = i
        if islands[maxIsland][1]:
            maxSize += 1
            
        return maxSize
            
        
    def findIslandSize(self,grid,start):
        border = set()
        stack = []
        stack.append(start)
        size = 1
        while stack:
            row, col = stack.pop()
            grid[row][col] = -1
            for x, y in [(row+1,col),(row,col+1),(row-1,col),(row,col-1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]): 
                    if grid[x][y] == 1:
                        stack.append((x,y))
                        size += 1
                        grid[x][y] = -1
                        
                    elif grid[x][y] == 0:
                        border.add((x,y))
        return size, border


