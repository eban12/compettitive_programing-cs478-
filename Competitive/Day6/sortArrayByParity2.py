def sortArrayByParityII(A):
        even = 0
        odd = 1
        sorted = [0] * len(A)
        for i in A:
            if i % 2 == 0:
                sorted[even] = i
                even += 2
            else:
                sorted[odd] = i
                odd += 2
        return sorted