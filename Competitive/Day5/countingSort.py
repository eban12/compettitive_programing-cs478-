def countSort(lst):
    large = max(lst)
    counter = [0] * (large + 1) 
    for i in lst:
        counter[i] += 1
    
    sorted = []
    for j in range(len(counter)):
        for k in range(counter[j]):
            sorted.append(j)
    
    return sorted

lst = [2,5,1,8,5,1,8,3,0,7]
print(countSort(lst))

