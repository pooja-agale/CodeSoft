print("_______CALCULATOR________\n")

num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
operator = input("Enter operator: ")

if operator == '+':
    sum = num1 + num2
    print("Addition: ", sum)
elif operator == '-':
    sub = num1 - num2
    print("Substraction: ", sub)
elif operator == '*':
    multi = num1 * num2
    print("Multiplication: ", multi)
elif operator == '/':
    div = num1 / num2
    print("Division: ", div)
elif operator == '%':
    per = num1 * num2 / 100
    print("Percent: ", per)
else:
    print("Invalid Input")


print("....THANK YOU....")
