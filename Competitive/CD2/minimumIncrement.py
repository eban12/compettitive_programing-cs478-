class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        moves = 0
        for i in range(1,len(A)):
            if A[i] <= A[i - 1]:
                t = abs(A[i] - A[i - 1]) + 1 
                moves += t
                A[i] += t
        return moves
