number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
unit_digit_1=number1%10
unit_digit_2=number2%10
unit_digit= unit_digit_1+unit_digit_2

if(unit_digit>0):
    if(unit_digit%2==0):
        print("The sum of the given unit digits of the inputs is even")
    else:
        print("The sum of the given unit digits of the inputs is odd ")
else:
    print("Unit digit is 0")
