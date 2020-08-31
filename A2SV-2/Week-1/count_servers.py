class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rows = [set() for _ in range(m)]
        cols = [set() for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i].add((i,j))
                    cols[j].add((i,j))
        
        ans = self.connectedBy(rows, set())
        ans = self.connectedBy(cols, ans)
        
        return len(ans)
        
    def connectedBy(self, direction, ans):
        for el in direction:
            if len(el) > 1:
                ans = ans.union(el)
        
        return ans
                                     
