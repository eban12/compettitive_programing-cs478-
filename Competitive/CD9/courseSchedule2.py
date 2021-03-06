class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses, pcount = self.getPrequisitesAndCount(numCourses, prerequisites)
        
        queue = collections.deque()
        for i in range(numCourses):
            if pcount[i] == 0:
                queue.append(i)
        
        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for i in courses[cur]:
                pcount[i] -= 1
                if pcount[i] == 0:
                    queue.append(i)
        
        if sum(pcount) == 0:
            return res
        return []
    
    def getPrequisitesAndCount(self,numCourses, prerequisites):
        courses = [set() for _ in range(numCourses)]
        pcount = [0 for _ in range(numCourses)]
        
        for i in prerequisites:
            courses[i[1]].add(i[0])
            pcount[i[0]] += 1
            
        return courses, pcount
