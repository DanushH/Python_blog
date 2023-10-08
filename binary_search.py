def binary_search(list, target):
    left, right = 0, len(list) - 1

    while left <= right:
        mid = left + (right - left) // 2  
        
        if list[mid] == target:
            return f"{target} is a square number" 
        elif list[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1 
    
    return f"{target} is not a square number" 


square_numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
target = 81
print(binary_search(square_numbers, target))
