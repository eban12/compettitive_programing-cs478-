# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    current = root
    p = None
    while current != None:
        p = current
        if current.val >= val:
            current = current.left
        else:
            current = current.right
    if p is None:
        root = TreeNode(val)
    elif p.val >= val:
        p.left = TreeNode(val)
    else:
        p.right = TreeNode(val)
    return root