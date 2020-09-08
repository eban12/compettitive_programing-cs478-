class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
          return nums
        n = len(nums)
        left = self.sortArray(nums[:n//2])
        right = self.sortArray(nums[n//2:])
        new = self.merge(left, right)
        return new
    
    def merge(self, a1, a2):
      i = 0
      j = 0
      new = []
      while i < len(a1) and j < len(a2):
        if a1[i] >= a2[j]:
          new.append(a2[j])
          j += 1
        else:
          new.append(a1[i])
          i += 1
      new += a1[i:]
      new += a2[j:]
      return new
