def insertion(lst):
    for i in range(len(lst)):
        temp = lst[i]
        for j in range(i,0,-1):
            if temp < lst[j - 1]:
                lst[j] = lst[j - 1]
                lst[j - 1] = temp