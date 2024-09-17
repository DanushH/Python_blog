def insertion_sort(list):
    LEN = len(list)

    for i in range(1, LEN):
        key = list[i]
        j = i - 1

        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1

        list[j + 1] = key

    print(list)


insertion_sort([100, 64, 81, 1, 25, 16, 4, 49, 9, 36])
