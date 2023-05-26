import re

# Read the file
file_name = "regex_sum_1433285.txt"  # Replace with the actual file name
with open(file_name, 'r') as file:
    data = file.read()

# Find all the numbers using regular expression
numbers = re.findall('[0-9]+', data)

# Convert the strings to integers and calculate the sum
sum_of_numbers = sum(int(number) for number in numbers)

# Print the sum
print("Sum:", sum_of_numbers)
