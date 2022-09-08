def try_parce_float(num):
    try:
        num = float(num)
    except:
        cond = "false"
        return cond
    else:
        cond = "true"
        return cond


title = "Welcome to my simple Calculator :)"
titleUpdate = title.center(130)
print(titleUpdate)

print("Your operators is: + , - , * , /")
print("Choice one of them")
print()
while True:
    a = input("Input your first number here:")
    try_parce_float(a)
    while True:
        if try_parce_float(a) == "true":
            a = float(a)
            break
        else:
            a = input("Input your first number here:")
            try_parce_float(a)

    operator = input("Input operator here:")
    if operator in ("+", "-", "*", "-"):
        pass
    else:
        print("wrong input,try again")
        operator = input("Input operator here:")

    b = input("Input your second number here:")
    while True:
        if try_parce_float(b) == "true":
            b = float(b)
            break
        else:
            b = input("Input your second number here:")
            try_parce_float(b)

    c = 0.0

    if operator == "+":
        c = a + b
        print(a, operator, b, "=", c)

    elif operator == "-":
        c = a - b
        print(a, operator, b, "=", c)

    elif operator == "*":
        c = a * b
        print(a, operator, b, "=", c)

    elif operator == "/":
        c = a / b
        print(a, operator, b, "=", c)

    another_cal = input("Would you like more calculations? (yes/no): ")
    if another_cal == "no":
        break
