# finance_calculator.py

# Step 1: Ask the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Step 2: Ask for user total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Step 3: Calculate monthly savings (income - expenses)
monthly_savings = monthly_income - monthly_expenses

# Step 4: Calculate projected savings after one year with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Step 5: Print results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
