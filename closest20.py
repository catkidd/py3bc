# Write a program to find a number closest to 0.

a = 100
b = 59
c = 78
closest = 0

if a < b and a < c:
    closest = a
    print(f"a({a}) is closest to 0")
elif b < c:
    closest = b
    print(f"b({b}) is closest to 0")
else:
    closest = c
    print(f"c({c}) is closest to 0")