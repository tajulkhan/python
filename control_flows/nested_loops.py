# Nested loops example: Printing a multiplication table (5x5)
for i in range(1, 6):  # Outer loop for rows
    for j in range(1, 6):  # Inner loop for columns
        print(f"{i * j}\t", end='')  # Print the product with a tab for spacing
    print()  # Move to the next line after each row
