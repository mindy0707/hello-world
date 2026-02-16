initial_population = float(input("Enter the initial number of organisms: "))
growth_rate = float(input("Enter the growth rate (e.g., 2 for doubling): "))
hours_per_growth = float(input("Enter the number of hours to achieve this growth rate: "))
total_hours = float(input("Enter the total number of hours the population grows: "))

population = initial_population

cycles = int(total_hours // hours_per_growth)

for i in range(cycles):
    population *= growth_rate

print("The predicted population is:", population)
