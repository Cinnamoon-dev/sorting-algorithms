def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

if __name__ == "__main__":
    arr = [7, 4, 1, 3, 5, 9, 2, 8, 6]
    print(bubble_sort(arr))
