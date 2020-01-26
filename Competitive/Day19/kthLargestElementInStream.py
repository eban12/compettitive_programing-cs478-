class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # self.candidates = 
        self.k = k
        self.buildHeap(nums)
        self.heapSort(nums)
        
        if len(nums) >= k:
            self.candidates = nums[:k]
        else:
            self.candidates = nums
        
        self.buildHeap(self.candidates)
            
    def add(self, val: int) -> int:
        if len(self.candidates) < self.k:
            self.candidates.append(val)
        
        elif val >= self.candidates[0]:
            self.candidates[0] = val
        
        self.percolateDown(self.candidates, 0, len(self.candidates) - 1)
        # self.buildHeap(self.candidates)
        
        return self.candidates[0]
        
    def percolateDown(self, lst, start, end):
        largest = 2 * start + 1
        while largest <= end:
            if largest + 1 <= end and lst[largest] > lst[largest + 1]:
                largest += 1

            if lst[start] > lst[largest]:
                lst[start], lst[largest] = lst[largest], lst[start]
                start = largest
                largest = 2 * start + 1
            else:
                return
    
    def buildHeap(self,lst):
        end = len(lst)
        start = end // 2
        while start >= 0:
            self.percolateDown(lst, start, end - 1)
            start -= 1
        
    def heapSort(self,heap):
        end = len(heap) - 1
        while end > 0:
            heap[0], heap[end] = heap[end], heap[0]
            end -= 1
            self.percolateDown(heap, 0, end)
            
        
            
        
    
            
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
