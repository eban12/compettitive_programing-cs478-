# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        res = 0
        stack = []
        if root is None:
            return 0
        stack.append(root)
        while len(stack) > 0:
            temp = stack.pop()
            if temp is not None:
                if temp.val >= L and temp.val <= R:
                    res += temp.val
                if temp.val > L:
                    stack.append(temp.left)
                if temp.val < R:
                    stack.append(temp.right)
        return res
