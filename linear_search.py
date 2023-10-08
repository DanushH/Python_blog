def linear_search(list, target):
    for i in list:
        if i == target:
            return f"{target} is in the list"

    return f"{target} is not in the list"


cube_numbers = [1, 8, 27, 64]
target = 27
print(linear_search(cube_numbers, target))
