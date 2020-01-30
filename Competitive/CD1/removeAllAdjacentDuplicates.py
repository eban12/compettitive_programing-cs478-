class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        while True:
            start = 0
            count = 1
            for i in range(1,len(s)):
                if s[i] == s[start]:
                    count += 1
                else:
                    count = 1
                    start = i
                
                if count == k:
                    end = start + k
                    s = s[:start] + s[end:]
                    count = 1
                    break
            if start == len(s) - 1 or len(s) < k:
                return s
