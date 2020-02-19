class Solution:
    import collections
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        setA = set()
        setB = set()
        for i in range(len(graph)):
            if i not in visited and not self.bfs(i,setA,setB,graph,visited):
                return False
        return True
        
    
    def bfs(self, start,setA,setB,graph,visited):
        visited.add(start)
        queue = collections.deque()
        queue.append((start,True))
        while queue:
            pos, Red = queue.popleft()
            if Red and pos in setB:
                return False
            elif Red:
                setA.add(pos)
            elif not Red and pos in setA:
                return False
            else:
                setB.add(pos)
                
            visited.add(pos)
            for j in graph[pos]:
                if j not in visited:
                    queue.append((j,not Red))
        
        return True
        
            
                
                    
        
        
