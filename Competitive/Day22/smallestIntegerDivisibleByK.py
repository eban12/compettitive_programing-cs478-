class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        
        temp = 1
        count = 1
        while temp % K != 0:
            temp = (temp % K) * (10 % K) + 1
            count += 1
        return count
        
