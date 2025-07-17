num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
oper = input("Choose the operation (+, -, *, /):")

match oper:
    case "+":
        num3 = num1 +num2
        print(f"The answer is{num3}")
    case "-":
        num3 = num1 - num2
        print(f"The answer is {num3}")
    case "*":
        num3 = num1 * num2
        print(f"The answer is {num3}")
    case "/":
        if num2 == 0:
            print("Cannot divide by Zero")
        else:
            num3 = num1 / num2
            print(f"The answer is {num3}")
