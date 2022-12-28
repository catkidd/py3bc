# Write a program to find a number closest to 0.

a = 100
b = 59
c = 78
closest = 0

if a < b and a < c:
    closest = a
    print(str(closest) + " is closest to 0")
elif b < c:
    closest = b
    print(str(closest) + " is closest to 0")
else:
    closest = c
    print(str(closest) + " is closest to 0")