def relativeSortArray(arr1, arr2):
        s = []
        for i in arr2:
            for j in range(arr1.count(i)):
                s.append(i)
                arr1.remove(i)
        return s + sorted(arr1)