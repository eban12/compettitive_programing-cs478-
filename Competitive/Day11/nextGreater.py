# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return []
        
        ans = [0]
        temp = []
        temp.append([head.val, 0])
        idx = 1
        current = head.next
        while current:
            ans += [0]
            t = current.val
            while temp and temp[-1][0] < t:
                ans[temp[-1][1]] = t
                temp.pop()
            temp.append([t,idx])
            current = current.next
            idx += 1
        return ans
