class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        maxAscii = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] + ord(s1[i-1]))
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return self.getAsciiSum(s1) + self.getAsciiSum(s2) - 2 * (dp[n][m])
    
    def getAsciiSum(self, s):
        total = 0
        for char in s:
            total += ord(char)
        return total
