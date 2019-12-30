class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations == []:
            return 0
        
        n = len(citations)
        l = 0
        r = n - 1
        while l < r:
            mid = (l + r) // 2
            if citations[mid] >= n - mid:
                r = mid
            else:
                l = mid + 1
        if citations[r] != 0:        
            return n - r
        else:
            return 0
            
