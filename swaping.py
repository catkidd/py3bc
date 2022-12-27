# To swap values of two variables 

a = 10
b = 20
print(f"Before swap a = {a} , b = {b}")
a = a + b
b = a - b
a = a - b
print(f"After swap a = {a} , b = {b}")