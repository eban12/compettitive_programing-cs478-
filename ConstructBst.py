# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        left = []
        right = []
        r = preorder[0]
        for i in preorder[1:]:
            if i < r:
                left.append(i)
            else:
                right.append(i)
        root = TreeNode(r)
        if len(left) > 0:
            root.left = self.bstFromPreorder(left)
        if len(right) > 0:
            root.right = self.bstFromPreorder(right)
        return root
