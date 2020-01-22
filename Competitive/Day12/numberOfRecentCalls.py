class RecentCounter:

    def __init__(self):
        self.calls = []
        
    def ping(self, t: int) -> int:
        self.calls.append(t)
        start = t - 3000
        n = self.findStart(start)
        return len(self.calls) - n
    
    def findStart(self, start):
        l = 0
        r = len(self.calls) - 1
        while l <= r:
            m = (l + r) // 2
            if self.calls[m] < start and self.calls[m + 1] >= start:
                return m + 1
            elif self.calls[m] < start and self.calls[m + 1] < start:
                l = m + 1
            else:
                r = m - 1
        return 0

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
