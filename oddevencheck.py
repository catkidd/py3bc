# Write a python script to check weather the number is even or odd.

num = int(input("Enter any number : "))

# method 1
if num % 2 == 0:
    print("Even") 
else:
    print("Odd")

# method 2
if num % 2:
    print("Odd") 
else:
    print("Even")
