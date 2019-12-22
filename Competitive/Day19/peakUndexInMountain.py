class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if A[0] > A[1]:
            return 0
        for i in range(1,len(A)):
            if A[i - 1] < A[i]  and (i + 1 == len(A) or A[i] > A[i + 1]):
                return i