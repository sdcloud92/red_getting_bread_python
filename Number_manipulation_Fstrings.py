# print(8 /3) = 2.66666666
# print(int(8 /3)) = 2

# How to round number
# print(round(8 / 3)) = 3

# Round to a specific decimal poitn

#vprint(round(8 / 3, 2)) = 2.67 rounds to two decimal places
# print(round(2.6666666, 2))

# Floor division
# print(8 // 3) #Floor division will give you an INTEGER answer instead of the standard FLOAT answer
# print(type(8 // 3))

# If we save the result of a calculation to a variable, can continue to perform calculations on the varibale
# result = 4 / 2

# result = 4 / 2 # if we want to divide the result by 2 again 
# result /= 2
# print(result)

# score = 0

# # User scores a point
# score += 1
# print(score)

#F strings: Make it eay to mix strings and data types
#print("Your score is" + str(score)) #Will get an error

# How to mix data types?

score = 0
height = 1.8
winning = True

#fstring type f infront of your string ""
print(f"Your score is {score}, your height is {height}, you are winning is {winning}")

