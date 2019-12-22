def mergeSort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])
    return merge(left,right)

def merge(left,right):
    sorted = []
    while len(left) > 0 and len(right) > 0:
        if right[0] > left[0]:
            sorted.append(left[0])
            left.pop(0)
        elif left[0] > right[0]:
            sorted.append(right[0])
            right.pop(0)
        elif right[0] == left[0]:
            sorted.append(right[0])
            sorted.append(left[0])
            left.pop(0)
            right.pop(0)
    return sorted + left + right