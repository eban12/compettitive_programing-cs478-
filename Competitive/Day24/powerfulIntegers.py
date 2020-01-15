class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = set()
        for i in range(20):
            for j in range(20):
                temp = (x ** i) + (y ** j)
                if temp <= bound:
                    ans.add(temp)
        return ans
                    
