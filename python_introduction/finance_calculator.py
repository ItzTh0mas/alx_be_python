Monthly_income = input("Enter your monthly income: $")
Monthly_expenses = input("Enter your total monthly expenses: $")
Monthly_savings = int(Monthly_income) - int(Monthly_expenses)

Proj_savings = Monthly_savings * 12 +(Monthly_savings * 12* 0.05)

print(f" Your monthly savings are ${Monthly_savings}.")
print(f"Your projected savings in one year, including interest is ${Proj_savings}")
