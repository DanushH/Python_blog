def quick_sort(list):
    if len(list) <= 1:
        return list

    pivot = list[len(list) // 2]
    left = [x for x in list if x < pivot]
    middle = [x for x in list if x == pivot]
    right = [x for x in list if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


list = [100, 64, 81, 1, 25, 16, 4, 49, 9, 36]
sorted_list = quick_sort(list)
print(sorted_list)
