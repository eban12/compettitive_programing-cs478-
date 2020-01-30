class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popPointer = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            
            while stack and popPointer < len(popped) and popped[popPointer] == stack[-1]:
                stack.pop()
                popPointer += 1
                
        return len(stack) == 0
