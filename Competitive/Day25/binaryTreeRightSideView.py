# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        stack = []
        cur = root
        depth = 0
        dic = {}
        while True:
            if cur:
                stack.append([cur,depth + 1])
                if depth not in dic:
                    dic[depth] = cur.val
                depth += 1
                cur = cur.right
            elif stack:
                temp = stack.pop()
                depth = temp[1]
                cur = temp[0].left
            else:
                break
        
        
        return dic.values()
