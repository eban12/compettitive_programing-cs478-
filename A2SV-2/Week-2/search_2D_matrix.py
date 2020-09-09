class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1
        while l <= r:
            mid = (r + l)//2
            x = mid // n
            y = mid % n
            # print(x,y)
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
                
