print("Welcome to Basic Calculator\n")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
print()
act = input("Enter function '+, -, *, /': ")
print()

if act == '+':
    print(num1 + num2)
elif act == '-':
    print (num1 - num2)
elif act == '*':
    print (num1 * num2)
elif act == '/':
    print (num1 / num2)
else:
    print("you did something wrong")
