def main():
    starting_salary = float(input("Enter the starting salary: "))
    percent_increase = float(input("Enter the percentage increase: "))
    years = int(input("Enter the number of years: "))

    salary = starting_salary

    print("Year   Salary")
    print("----------------")

    for year in range(1, years + 1):
        print(year, "   ", salary)
        salary = salary + (salary * percent_increase / 100)

main()
