class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        heap = [-i for i in dic.values()]
        heapq.heapify(heap)
        
        desiredFrequencies = set()
        for i in range(k):
            desiredFrequencies.add(-(heapq.heappop(heap)))
        
        ans = []
        i = 0
        key = list(dic.keys())
        while len(ans) < k and i < len(key):
            if dic[key[i]] in desiredFrequencies:
                ans.append(key[i])
            i += 1
        
        return ans
        
