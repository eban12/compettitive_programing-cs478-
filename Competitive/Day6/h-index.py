def hIndex(citations):        
        n = len(citations)
        count = [0 for x in range(n)]
        for i in citations:
            if i > n:
                count[n - 1] += 1
            elif i == 0:
                pass
            else:
                count[i - 1] += 1
        
        temp = 0
        for i in range(n - 1, -1, -1):
            count[i] += temp
            temp = count[i]
            if i + 1 <= count[i]:
                return i + 1
        return 0