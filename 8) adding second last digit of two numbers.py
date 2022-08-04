number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))

# second last digit of number 1
last_num1=number1//10

second_last_number1=last_num1%10

# second last digit of number 2
last_num2=number2//10

second_last_number2=last_num2%10

#printing result

last_digit=second_last_number1+second_last_number2
print(last_digit)

