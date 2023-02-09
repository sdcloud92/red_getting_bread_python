#1)What is RANDOMISATION? (used alot in games)

# To generate a random integer:
#     randint(a,b)

import random #Must be called before running any random code
# random_integer = random.randint(1,10) #This code will give us a random number between 1 - 10
# print(random_integer)

# 2)What is a MODULE
# split code up into individual modules responsible for different parts of the code. eg building a car, some people work on wheel moduel, engine module etc

# 3)How to create random floating point numbers?
# random_float = random.random() #will always print random numbers between 0-1
# print(random_float)

#BUT how to create a random float between 0 - 5?
random_float = random.random() * 5
print(random_float)