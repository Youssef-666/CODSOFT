x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
op = input("Pick the operation (+, -, *, /): ")

if (op == '+'):
    res = x+y
elif (op == '-'):
    res = x-y
elif (op == '*'):
    res = x*y
elif (op == '/'):
    res = x/y

print(f"The result is: {res}")