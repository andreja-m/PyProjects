var = int(input("Lenght Of Sequence: [+] "))

def Fib(n):
    if n<0:
        print("Incorect input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)

print(Fib(var))
