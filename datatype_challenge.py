#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Hint:
# Try to find out the data type of two_digit_number.
# Think about what you learnt about subscripting.
# Think about type conversion.

chosen_no = input("Choose a two digit number: ")
#print(type(chosen_no))

#new_chosen_no = int(chosen_no)

first_digit = chosen_no[0]
second_digit = chosen_no[1]

# print(first_digit)
# print(second_digit)

result = int(first_digit) + int(second_digit)
print(result)
