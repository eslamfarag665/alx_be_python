monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter your total monthly expenses:"))
monthly_savings = float(monthly_income) - float(monthly_expenses)
Projected_Savings = float(monthly_savings) * 12 + float(monthly_savings) * 12 * 0.05
print("Your monthly savings are" ,monthly_savings)
print("Projected savings after one year, with interest, is:" ,Projected_Savings)
