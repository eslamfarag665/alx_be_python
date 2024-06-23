monthly_inc = int(input("Enter your monthly income:"))
monthly_exp = int(input("Enter your total monthly expenses:"))
Monthly_Sav = monthly_inc-monthly_exp
Projected_Savings = int(Monthly_Sav * 12 + (Monthly_Sav * 12 * 0.05))
print("Your monthly savings are" ,Monthly_Sav)
print("Projected savings after one year, with interest, is:" ,Projected_Savings)