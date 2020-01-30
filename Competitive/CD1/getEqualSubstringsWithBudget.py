class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = []
        start = 0
        count = 0
        costSum = 0
        ans = 0
        for i in range(len(s)):
            cost = abs(ord(s[i]) - ord(t[i]))
            costs.append(cost)
            costSum += cost
            
            while costSum > maxCost and len(costs) > start:
                if ans < count:
                    ans = count
                costSum -= costs[start]
                count -= 1
                start += 1

            count += 1
            
        if count > ans:
            ans = count

        return ans 
