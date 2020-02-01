# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack = []
        depth = 0
        root = None
        i = 0
        while i < len(S):
            if S[i] == '-':
                depth += 1
                i += 1
            else:
                start = i
                while i < len(S) and S[i] != '-':
                    i += 1
                val = S[start:i]
                if stack == []:
                    parent = TreeNode(val)
                    stack.append((parent,depth))
                    root = parent
                elif stack[-1][1] < depth:
                    parent, d = stack.pop()
                    kid = TreeNode(val)
                    parent.left = kid
                    stack.append((parent,d))
                    stack.append((kid,depth))
                elif stack[-1][1] == depth:
                    kid1, d = stack.pop()
                    kid2 = TreeNode(val)
                    parent, dp = stack.pop()
                    parent.left = kid1
                    parent.right = kid2
                    stack.append((parent,dp))
                    stack.append((kid2,d))
                else:
                    while stack[-1][1] >= depth:
                        stack.pop()
                    kid = TreeNode(val)
                    parent, d = stack.pop()
                    parent.right = kid
                    stack.append((parent,d))
                    stack.append((kid,depth))
                depth = 0
        
        return root
