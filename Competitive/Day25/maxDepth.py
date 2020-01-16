class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        
        max_Depth = 0
        for i in root.children:
            max_Depth = max(max_Depth, self.maxDepth(i))
            
        return max_Depth + 1
