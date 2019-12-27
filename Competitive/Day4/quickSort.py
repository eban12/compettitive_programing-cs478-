def partition(lst, low, high):
    i = low - 1
    pivot = lst[high]
    for j in range(low, high):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1


def quickSort(lst, low, high):
    if low < high:
        pi = partition(lst, low, high)
        quickSort(lst, low, pi - 1)
        quickSort(lst, pi + 1, high)
    return lst


arr = [10, 7, 5, 8, 9, 1, 5]
n = len(arr)
print(quickSort(arr, 0, n - 1))
print(arr)
