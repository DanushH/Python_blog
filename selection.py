def selection_sort(list):
    LEN = len(list)

    for i in range(LEN):
        min_index = i

        for j in range(i + 1, LEN):
            if list[j] < list[min_index]:
                min_index = j

        list[i], list[min_index] = list[min_index], list[i]

    print(list)


selection_sort([100, 64, 81, 1, 25, 16, 4, 49, 9, 36])
