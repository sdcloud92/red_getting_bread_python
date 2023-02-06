# Write a program that prints the numbers from 1 - 100.
# For each multiple of three print "Fizz" instead of the number. 
# For multiples of five print "Buzz" instead of the number. 
# If a number is a multiple of three and five then print "FizzBuzz".

# Solving this problem requires 2 key components: looping and conditionals.
# We're going to write a simplified program only using the conditional portion 
# that will take any given number that we provide and print the Fizz-Buzz value. 
# Here's how it will work:


value = int(input("Enter an integer value: "))

if value % 5 == 0 and value % 3 == 0:
    print("FizzBuzz")
elif value % 3 == 0:
    print("Fizz")
elif value % 5 == 0:
    print("Buzz")
else:
    print(value)
    
