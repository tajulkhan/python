# Loop through a range of numbers from 1 to 5
for i in range(1, 6):
    print(f"Iteration {i}")

# While loop 
count = 1
while count <= 5:
    print(f"Iteration {count}")
    count += 1  

# Example with break statement
for i in range(1, 11):
    if i == 6:
        print("Breaking the loop at 6")
        break  # Exit the loop
    print(i)
