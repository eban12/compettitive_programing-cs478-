class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        import math
        total = 0
        for i in range(1,int(math.sqrt(num)) + 1):
            if num % i == 0:
                total += i
                temp = num / i
                if temp < num:
                    total += temp
        return total == num
