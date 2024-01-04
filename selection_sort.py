def selection_sort(array):
    length = len(array)

    for i in range(length - 1):
        minimum = i

        for j in range(i + 1, length):
            if array[minimum] > array[j]:
                minimum = j

        array[i], array[minimum] = array[minimum], array[i]

    return array

if __name__ == "__main__":
    arr = [7, 4, 1, 3, 5, 9, 2, 8, 6]
    print(selection_sort(arr))

