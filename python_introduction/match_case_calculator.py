num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
oper = input("Choose the operation (+, -, *, /):")

match oper:
    case "+":
        num3 = num1 +num2
        print(str(num3))
    case "-":
        num3 = num1 - num2
        print(str(num3))
    case "*":
        num3 = num1 * num2
        print(str(num3))
    case "/":
        num3 = num1 / num2
        print(str(num3))
