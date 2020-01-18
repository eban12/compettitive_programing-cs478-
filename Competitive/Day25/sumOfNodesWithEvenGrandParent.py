# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        evenNodes = []
        stack = []
        current = root
        while True:
            
            if current:
                stack.append(current)
                if current.val % 2 == 0:
                    evenNodes.append(current)
                current = current.left
            elif stack:
                current = stack.pop().right
            else:
                break
        
        total = 0
        for node in evenNodes:
            if node.left:
                if node.left.left:
                    total += node.left.left.val
                
                if node.left.right:
                    total += node.left.right.val
            
            if node.right:
                if node.right.left:
                    total += node.right.left.val
                
                if node.right.right:
                    total += node.right.right.val
                    
        return total
