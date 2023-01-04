"""Write a program that prints the numbers from 1 to n, 
where n is the input provided to the program. But for multiples of three print "Fizz" instead of the number, 
and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz"."""

# approach 1 -->
def fizzbuzz():
    for i in range(1, 101):
        # if i % 3 == 0 and i % 5 == 0:
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)


fizzbuzz()
