import math, copy

def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    aux = copy.deepcopy(arr)

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            aux[k] = arr[i]
            i += 1
            k += 1
        else:
            aux[k] = arr[j]
            j += 1
            k += 1

    while i <= mid:
        aux[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        aux[k] = arr[j]
        j += 1
        k += 1

    for i in range(len(arr)):
        arr[i] = aux[i]


def merge_sort(arr, left, right):
    if left >= right:
        return

    middle = (left + right) // 2

    merge_sort(arr, left, middle)
    merge_sort(arr, middle + 1, right)

    merge(arr, left, middle, right)

if __name__ == "__main__":
    arr = [7, 4, 1, 3, 5, 9, 2, 8, 6]
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)
