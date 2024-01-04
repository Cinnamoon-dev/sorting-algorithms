def insertion_sort(array):
    size = len(array)

    for i in range(size):
        k = i

        while k > 0:
            if array[k] < array[k - 1]:
                array[k - 1], array[k] = array[k], array[k - 1]
            k -= 1

        return array

if __name__ == "__main__":
    arr = [7, 4, 1, 3, 5, 9, 2, 8, 6]
    print(insertion_sort(arr))
