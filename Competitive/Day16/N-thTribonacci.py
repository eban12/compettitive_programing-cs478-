class Solution:
    def tribonacci(self, n: int, a=0, b=1, c=1) -> int:
        if n <= 1:
            return n
        if n == 2:
            return c
        return self.tribonacci(n-1, b, c, a + b + c)