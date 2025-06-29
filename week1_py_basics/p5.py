# Taxation Problem 
 
# Level 1 - accepting inputs, salary calculation
emp_name = input("enter employee name: ")
empID = input("enter emploeye ID: ")
emp_BMS = int(input("enter basic monthly salary: "))
emp_SMA = int(input("enter special monthly allowance: "))
emp_bonus_percentage = int(input("enter bonus percentage: "))

gross_monthly_salary = emp_BMS + emp_SMA
emp_bonus = (emp_bonus_percentage / 100) * gross_monthly_salary
annual_gross_salary = (gross_monthly_salary * 12) + emp_bonus

print(f"Employee name: {emp_name}")
print(f"Employee ID: {empID}")
print(f"Employee basic monthly salary: {emp_BMS}")
print(f"Employee special monthly allowance: {emp_SMA}")
print(f"Employee bonus percentage: {emp_bonus_percentage}%")
print(f"Gross monthly salary: {gross_monthly_salary}")
print(f"Bonus: {emp_bonus}")
print(f"Annual gross salary: {annual_gross_salary}")

# Level 2 - taxable income calculation
standard_deduction = 50000 #rupees
taxable_income = annual_gross_salary - standard_deduction
print(f"Annual gross salary: {annual_gross_salary}")
print(f"Standard deduction: {standard_deduction}")
print(f"Taxable income: {taxable_income}")

# Level 3 - tax and rebate calculation







# Level 4  - net salary calculation








# Level 5 - report generation