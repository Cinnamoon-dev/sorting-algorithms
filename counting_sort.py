def counting_sort(array):
    max_value = max(array)
    count = [0] * max_value
    result = [0] * len(array)

    for i in range(len(array)):
        count[array[i] - 1] += 1

    j = 0
    for i in range(len(count)):
        if count[i] > 0:
            for k in range(0, count[i]):
                result[j] = i + 1
                j += 1

    return result

if __name__ == "__main__":
    arr = [7, 4, 1, 3, 5, 9, 2, 8, 6]
    print(counting_sort(arr))
