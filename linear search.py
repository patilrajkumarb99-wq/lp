# Linear Search Program

# List of numbers
numbers = [10, 20, 30, 40, 50]

# Number to search
search = int(input("Enter number to search: "))

# Variable to check found or not
found = False

# Loop through list
for i in range(len(numbers)):
    if numbers[i] == search:
        print("Number found at position", i + 1)
        found = True
        break

# If number not found
if found == False:
    print("Number not found")
