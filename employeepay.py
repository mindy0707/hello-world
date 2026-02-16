hourly_wage = float(input("What is hourly wage?"))
regular_hours_worked = float(input("What are the regular hours worked?"))              
overtime_hours = float(input("How many overtime hours?"))
overtime_pay = overtime_hours * (1.5 * hourly_wage)
employee_weekly_pay = (hourly_wage * regular_hours_worked) + overtime_pay
print(f"Total weekly pay for the time period is ${employee_weekly_pay:.2f}")
