# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#1 convert age from str to an int
age_as_int = int(age)

#2 calculate no of years left
years_remaining = 90 - age_as_int

#3 calculate no of days left
days_remaining = years_remaining * 365 

#4 calculate no of weekss left
weeks_remaining = years_remaining * 52

#5 calculate no of months left
months_remaining = years_remaining * 12

#Check code so far 

#print(months_remaining)

message = (f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")

print(message)