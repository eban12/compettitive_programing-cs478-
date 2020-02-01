class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        students = [[] for _ in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1:
                    students[i].append(j)
        
        circles = 0
        visited = set()
        for k in range(len(students)):
            if k not in visited:
                self.dfs(k,students,visited)
                circles += 1
        
        return circles
        
    
    def dfs(self,j,students,visited):
        visited.add(j)
        for i in students[j]:
            if i not in visited:
                self.dfs(i,students,visited)
