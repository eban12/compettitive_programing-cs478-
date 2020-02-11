class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        dic = {}
        def helper(i, B, C, sizeB, sizeC):
            if (B % (100),C % (100),sizeB,sizeC) in dic:
                return dic[(B % (100),C % (100),sizeB,sizeC)]
            if sizeB + sizeC >= len(A):
                if sizeB == 0 or sizeC == 0:
                    return False
                return (B  / sizeB) == (C / sizeC)
                
            
            ans = (helper(i + 1, B + A[i], C, sizeB+1, sizeC)) or (helper(i + 1, B, C + A[i], sizeB, sizeC + 1))
            dic[(B % (100),C % (100),sizeB,sizeC)] = ans
            return ans
        return helper(0,0,0,0,0)
