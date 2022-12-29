# Write a program to store first 10 even number and first 10 odd number in a list and print their sum.

elist = []
olist = []
esum = 0
osum = 0

for i in range(1, 21):
    if i % 2:
        olist.append(i)
        osum += i

for j in range(1, 21):
    if j % 2 == 0:
        elist.append(j)
        esum += j

print(olist)
print(osum)
print(elist)
print(esum)
print(esum + osum)