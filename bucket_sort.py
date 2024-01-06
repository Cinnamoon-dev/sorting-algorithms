import math

def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

def bucket_sort(array):
    buckets = [[]] * len(array)
    ordered_array = []

    for i in array:
        buckets[math.floor(len(array) * i)].append(i)

    for i in range(0, len(buckets)):
        buckets[i] = bubble_sort(buckets[i])

    for i in buckets:
        while len(i) != 0:
            ordered_array.append(i.pop(0))

    return ordered_array

if __name__ == "__main__":
    arr =[0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print(bucket_sort(arr))
