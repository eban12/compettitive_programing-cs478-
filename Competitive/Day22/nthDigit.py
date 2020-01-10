class Solution:
    def findNthDigit(self, n: int) -> int:
        l = 1
        count = 9
        start = 1
        while n > l * count:
            n -= l * count
            l += 1
            count *= 10
            start *= 10
        start += (n - 1) // l
        start = str(start)
        return start[(n - 1) % l]
