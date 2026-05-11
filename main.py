from fun import add, sub, div, square

ans = input("Enter '+', '-', '*', or '/' to get result: ")

if ans not in ['+','-','*','/']:
    print('There is a mistake. Please select +, -, *, or /')

else:
    if ans == "*":
        a = float(input("Enter the number = "))
    else:
        a = float(input("Enter the first number = "))
        b = float(input("Enter the second number = "))

    if ans == "+":
        print(f"This is your output {add(a, b)}")

    elif ans == "-":
        print(f"This is your output {sub(a, b)}")

    elif ans == "*":
        print(f"This is your output {square(a)}")

    elif ans == "/":
        print(f"This is your output {round(div(a, b), 2)}")

    else:
        print("There is a mistake. Please select +, -, *, or /")