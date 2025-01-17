# CREATE
numbers = list()    # numbers = []


# INSERT
# Insert a range of values
for i in range(1, 11, 2):     # Odd numbers from 1 to 10
    numbers.append(i)
# Insert a value at specific index
numbers.insert(0, 150) # Insert 150 at the 0th index
# Insert a value at the end
numbers.append(600)
# Insert multiple values at the end
numbers.extend([2, 2, 2, 2, 2])


# RETRIEVE
# Read entire array
print("Initial array:", numbers)
# Read a range of values
print("Sliced array:", numbers[2:-2]) # 3rd to 2nd last elements 
# Read single value
print("1st element: ", numbers[0])
print("Last element:", numbers[-1], end="\n\n")


# SEARCH & UPDATE
# Search the 1st occurence of a value
SEARCH_VALUE = 600

if SEARCH_VALUE in numbers:
    print(f"{SEARCH_VALUE} found at index {numbers.index(SEARCH_VALUE)}")
    # Update the found value to 20
    numbers[numbers.index(SEARCH_VALUE)] = 2
else:
    print(f"{SEARCH_VALUE} not found")

print("Updated array: ", numbers, end="\n\n")

# Search all occurences of a value
SEARCH_VALUE = 2

for index, element in enumerate(numbers):
    if element == SEARCH_VALUE:
        print(f"{SEARCH_VALUE} found at index {index}")


# DELETE
# Delete the 1st occurence of a value
DELETE_VALUE = 150

if DELETE_VALUE in numbers:
    numbers.remove(DELETE_VALUE)
    print(f"\n{DELETE_VALUE} removed")
else:
    print(f"\n{DELETE_VALUE} not found")

# Delete all occurences of a value
DELETE_VALUE = 2
result = []

for element in numbers:
    if element != DELETE_VALUE:
        result.append(element)

print("New array after deleting: ", result, "\n")

# Delete all occurences of a value - inplace - two pointer
# DELETE_VALUE = 2
# counter = 0
#
# for index in range(len(numbers)):
#     if numbers[index] != DELETE_VALUE:
#         numbers[counter] = numbers[index]
#         counter += 1
#
# del numbers[counter:]   # Trim the list to exclude remaining elements

print("Final array: ", numbers)

