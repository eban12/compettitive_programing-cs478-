class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(i):
            for j in graph[i]:
                if j not in self.visited:
                    self.visited.add(j)
                    self.moves += 1
                    dfs(j)
                    
        graph = {}
        n = len(stones)
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    if i in graph:
                        graph[i].append(j)
                    else:
                        graph[i] = [j]
                    
                    if j in graph:
                        graph[j].append(i)
                    else:
                        graph[j] = [i]
                        
        self.visited = set()
        self.moves = 0
        for i in graph:
            if i not in self.visited:
                self.visited.add(i)
                dfs(i)
        
        
        return self.moves
