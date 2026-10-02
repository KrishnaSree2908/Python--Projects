print("------ EMPLOYEE PAYROLL SYSTEM ------")

name = input("Enter Employee Name: ")

try:
    basic_salary = float(input("Enter Basic Salary: "))
    if basic_salary <= 0:
        print("❌ Invalid salary")
        exit()
except:
    print("❌ Invalid input")
    exit()

# Salary calculations
hra = 0.20 * basic_salary   # House Rent Allowance
da = 0.10 * basic_salary    # Dearness Allowance
tax = 0.05 * basic_salary   # Tax deduction

gross_salary = basic_salary + hra + da
net_salary = gross_salary - tax

# Output
print("\n------ SALARY DETAILS ------")
print("Employee Name:", name)
print("Basic Salary:", basic_salary)
print("HRA (20%):", hra)
print("DA (10%):", da)
print("Tax (5%):", tax)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)