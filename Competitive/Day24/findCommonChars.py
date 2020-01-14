def find(A):

    # sol1 using dictionary
    # slower 

    ans = {}
    for i in A[0]:
        minCount = 2 ** 32
        for j in A:
            print(i, j)
            minCount = min(j.count(i), minCount)
        if i not in ans and minCount != 0:
            ans[i] = minCount
    
    temp = []
    for key in ans.keys():
        temp.append([key] * ans[key])
    
    return temp

    # sol2 without using dictionary
    # faster than sol1

    ans = []
    for i in A[0]:
        minCount = 1000
        for j in A:
            count = j.count(i)
            if count == 0:
                minCount = 0
                break
            minCount = min(count, minCount)
        if i not in ans and minCount != 0:
            for k in range(minCount):
                ans.append(i)
    return ans

find(["bella", "label", "calll"])