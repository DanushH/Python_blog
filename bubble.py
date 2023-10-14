def bubble_sort(list):
    LEN = len(list) - 1

    for i in range(LEN):
        swapped = False

        for j in range(LEN - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True

        if swapped == False:
            break

    print(list)


bubble_sort([100, 64, 81, 1, 25, 16, 4, 49, 9, 36])
