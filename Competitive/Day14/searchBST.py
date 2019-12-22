# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def searchBST(root: TreeNode, val: int) -> TreeNode:
    current = root
    while current != None and current.val != val:
        if current.val > val:
            current = current.left
        else:
            current = current.right
    return current