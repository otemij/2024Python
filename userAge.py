# Ask for the user's age
age = int(input("Enter your age: "))

# Keep asking until a valid age is entered
while age <= 0:
    print("Please enter a valid positive age.")
    age = int(input("Enter your age: "))

print(f"Thank you! Your age is {age}.")
