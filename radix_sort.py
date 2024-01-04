def get_digit(number: int, digit: int):
    """
        digit == 0 returns unit digit
        digit == 1 returns tens digit and so on

        if there is no digit in that position returns None
    """
    if digit > len(str(number)) - 1:
        return None

    return int(str(number)[-(digit + 1)])

def bubble_sort_digit(array, digit):
    for i in range(0, len(array)):
        for j in range(0, len(array) - i - 1):
            if get_digit(array[j], digit) is None and get_digit(array[j + 1], digit) is None:
                continue

            if get_digit(array[j], digit) is None and get_digit(array[j + 1], digit) is not None:
                continue

            if get_digit(array[j], digit) is not None and get_digit(array[j + 1], digit) is None:
                array[j], array[j + 1] = array[j + 1], array[j]
                continue

            if get_digit(array[j], digit) > get_digit(array[j + 1], digit):
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

def radix_sort(array):
    """
        Ordena os elementos processando digito por digito.

        Encontra o maior elemento. Ele vai ditar quantas iterações vão acontecer.
        Ordena os elementos com base no digito das unidades, dezenas, centenas, ...
        Ordena-se usando um algoritmo de ordenação estável
    """
    largest_length = len(str(max(array)))

    for i in range(0, largest_length):
        array = bubble_sort_digit(array, i)

    return array

if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print(radix_sort(arr))
