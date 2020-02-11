class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        dic = {}
        
        def helper(i, Bsum, Csum, sizeB, sizeC):
            if (Bsum % (100),Csum % (100),sizeB,sizeC) in dic:
                return dic[(Bsum % (100),Csum % (100),sizeB,sizeC)]
            
            if sizeB + sizeC >= len(A):
                if sizeB == 0 or sizeC == 0:
                    return False
                return (Bsum  / sizeB) == (Csum / sizeC)  
        
            ans = (helper(i + 1, Bsum + A[i], Csum, sizeB+1, sizeC)) or (helper(i + 1, Bsum, Csum + A[i], sizeB, sizeC + 1))
            dic[(Bsum % (100),Csum % (100),sizeB,sizeC)] = ans
            return ans
        
        return helper(0,0,0,0,0)
