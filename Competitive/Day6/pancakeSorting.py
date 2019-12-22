def pancakeSort(A):
        flips = []
        n = len(A)    
        while n > 0:
            max_index = 0
            for i in range(n):
                if A[max_index] < A[i]:
                    max_index = i
            if max_index != 0 and max_index + 1 != n:
                flips.append(max_index + 1)
            if n != max_index + 1:    
                flips.append(n)
            A = A[:max_index + 1][::-1] + A[max_index + 1:]                 
            A = A[::-1][:n - 1]
            n = len(A)
        return flips