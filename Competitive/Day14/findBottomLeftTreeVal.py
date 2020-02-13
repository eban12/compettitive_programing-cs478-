# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return root.val
        
        nodesLevel = []
        queue = collections.deque()
        queue.append([root,0])
        height = 0
        while queue:
            cur = queue.popleft()
            nodesLevel.append(cur)
            if cur[0].left:
                queue.append([cur[0].left, cur[1] + 1])
                
            if cur[0].right:
                queue.append([cur[0].right, cur[1] + 1])
            
            if cur[1] > height:
                height = cur[1]
            
        for i in range(len(nodesLevel)-1,-1,-1):
            if nodesLevel[i][1] != height:
                return nodesLevel[i+1][0].val
        
