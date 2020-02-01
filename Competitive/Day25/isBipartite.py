class Solution:
    import collections
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        setA = set()
        setB = set()
        for i in range(len(graph)):
            if i not in visited:
                self.bfs(i,setA,setB,graph,visited)
        
        for i in setA:
            if i in setB:
                return False
        return True
    
    def bfs(self, start,setA,setB,graph,visited):
        visited.add(start)
        queue = collections.deque()
        queue.append((start,True))
        while queue:
            pos, color = queue.popleft()
            if color:
                setA.add(pos)
            else:
                setB.add(pos)
            visited.add(pos)
            for j in graph[pos]:
                if j not in visited:
                    queue.append((j,not color))
        
        
        
            
                
                    
        
        
