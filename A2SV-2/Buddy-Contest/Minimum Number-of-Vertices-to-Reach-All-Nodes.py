class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {key:[] for key in range(n)}
        for frm, to in edges:
            graph[to].append(frm)
        
        ans = []
        for key, val in graph.items():
            if not val:
                ans.append(key)
        return ans
