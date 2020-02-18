class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for word in words:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        
        heap = []
        for key, value in dic.items():
            heap.append((-value, key))
        
        heapq.heapify(heap)
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans
