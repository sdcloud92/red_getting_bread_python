# age 18 and above pay adult price
# 18 below pay the junior price

# <= 18 $7
# > 18 $12

# standard if /else statement
# if condition:
#     do this
# else:
#     do this

# Nested if / else statement
# Once first condition is passed, check for another condition
# if condition:
#     if another condition:
#         do this
#         else:
#             do this
# else:
#     do this

# height = int(input("How tall are you? "))
# print(height)

# if height >= 120:
#     print("You can ride the rollercoster.")
#     age = int(input("How old are you? "))
#     if age >= 18:
#         print("Your ticket costs £12")
#     else:
#         print("Your ticket costs £7")
# else:
#     print("Sorry you are a shorty, you cannot ride")
    
# if / elif / else
# elif allows as many conditions as you want

# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do this

height = int(input("How tall are you? "))
print(height)

if height >= 120:
    print("You can ride the rollercoster.")
    age = int(input("How old are you? "))
    if age < 12:
        print("Your ticket is £5")
    elif age <= 18:
        print("Your ticket costs £7")
    else:
        print("Your ticket costs £12")
else:
    print("Sorry you are a shorty, you cannot ride")
    