import random

# Initialize an empty list to store the values
values = []

# Generate 10 random values and store them in the list
for i in range(10):
  value = random.randint(1, 100)  # Generate a random integer between 1 and 100
  values.append(value)

# Sort the values list so that the even values come before the odd values
values.sort()

# Determine whether the first value is even or odd
first_value = values[0]

# Separate the even and odd values
even_values = []
odd_values = []
for value in values:
  if value % 2 == 0:
    even_values.append(value)
  else:
    odd_values.append(value)

# Sort the values in odd/even order
sorted_values = []
if first_value % 2 == 0:
    # Append the even values followed by the odd values
    for i in range(len(even_values)):
        sorted_values.append(even_values[i])
        if i < len(odd_values):
            sorted_values.append(odd_values[i])
else:
    # Append the odd values followed by the even values
    for i in range(len(odd_values)):
        sorted_values.append(odd_values[i])
        if i < len(even_values):
            sorted_values.append(even_values[i])

# Print the values
print(values)
print(odd_values)
print(even_values)
print(sorted_values)
