def partition(arr, low, high):
    pivot = low

    for i in range(low, high):
        if arr[i] < arr[low]:
            pivot += 1
            arr[pivot], arr[i] = arr[i], arr[pivot]

    arr[low], arr[pivot] = arr[pivot], arr[low]
    return pivot

def quick_sort(arr, low, high):
    if low >= high:
        return arr

    pivot = partition(arr, low, high)

    quick_sort(arr, low, pivot)
    quick_sort(arr, pivot + 1, high)

    return arr

if __name__ == "__main__":
    arr = [7, 4, 1, 3, 5, 9, 2, 8, 6]
    print(quick_sort(arr, 0, len(arr)))
