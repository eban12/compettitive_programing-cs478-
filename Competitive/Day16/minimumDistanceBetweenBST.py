# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        valuesInOrder = []
        self.inorder(root, valuesInOrder)
        
        ans = 2 ** 32
        for i in range(len(valuesInOrder) - 1):
            ans = min(ans, valuesInOrder[i + 1] - valuesInOrder[i])
        return ans
    
    def inorder(self, root, lst):
        if not root: return
        
        self.inorder(root.left,lst)
        lst.append(root.val)
        self.inorder(root.right,lst)
    
        
