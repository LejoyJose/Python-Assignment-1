number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
sum=number1+number2
if(sum>0):
    if(sum%2==0):
        print("The sum of the given inputs is even")
    else:
        print("The Sum of given inputs is odd ")
else:
    print("The sum is 0")
