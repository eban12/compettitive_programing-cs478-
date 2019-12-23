class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if T == []:
            return []
        
        res = [0] * len(T)
        stack = []
        for i, temp in enumerate(T):
            if stack == [] or stack[-1][1] > temp:
                stack.append([i, temp])
            else:
                while stack and stack[-1][1] < temp:
                    s_inx, s_val = stack.pop()
                    res[s_inx] = abs(i - s_inx)
                stack.append([i, temp])
        return res 
