initial_height = float(input("Enter the initial height of the drop: "))
bounces = int(input("Enter the number of bounces: "))

index = float(input("Enter the bounciness index (e.g., 0.6): "))

total_distance = initial_height

current_height = initial_height * index

for i in range(bounces):
    total_distance += current_height * 2
    current_height *= index
print("The total distance traveled is:", total_distance)
