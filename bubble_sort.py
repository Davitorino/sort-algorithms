
def bubble_sort(arr):
    n = len(arr)
    for j in range(1, n):
        change = False
        for i in range(n - j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change = True
        if not change:
            break
    return arr
