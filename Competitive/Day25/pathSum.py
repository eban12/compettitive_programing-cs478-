class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        stack = [[root, 0]]
        while stack:
            temp = stack.pop()
            current = temp[0]
            expected = temp[1]
            if current:
                expected += current.val
                if not current.left and not current.right:
                    if expected == sum:
                        return True

                if current.right:
                    stack.append([current.right, expected])

                if current.left:
                    stack.append([current.left, expected])
        return False
