# Write a program to store first 10 even number and first 10 odd number in a list and print their sum.

eolist = []
sum = 0


for i in range(1, 21):
    if i % 2:
        eolist.append(i)
    else:
        eolist.append(i)
    sum += i


print(eolist)
print(f"The sum of first 10 even and first 10 odd number is: {sum} ")
