square_numbers = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Iterating over keys
for key in square_numbers:
    print(key)

# Iterating over values
for value in square_numbers.values():
    print(value)

# Iterating over key-value pairs
for key, square in square_numbers.items():
    print(f"{key}: {square}")
