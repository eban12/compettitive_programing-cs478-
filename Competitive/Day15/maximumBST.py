# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructMaximumBinaryTree(nums: List[int]) -> TreeNode:
    if nums == []:
        return None
    else:
        m = max(nums)
        idx = nums.index(m)
        root = TreeNode(m)
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx + 1:])
        return root