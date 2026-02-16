source_file = input("Enter the name of the file to copy from: ")
target_file = input("Enter the name of the file to copy to: ")

with open(source_file, "r") as infile:
    contents = infile.read()

with open(target_file, "w") as outfile:
    outfile.write(contents)

print("File copied successfully.")
