# Start of the ice cream ordering program

# Ask for the type of serving
serving = input("Cup (50p) or Cone (80p)? ").lower()
if serving == "cone":
    serving_cost = 0.80
else:
    serving_cost = 0.50

# Ask for the number of scoops
scoops = int(input("How many scoops (1 to 4)? "))
scoops_cost = scoops * 1.00

# Ask if they want a flake
flake = input("Add a flake for 40p? (yes/no) ").lower()
if flake == "yes":
    flake_cost = 0.40
else:
    flake_cost = 0.00

# Ask if they want chocolate sprinkles
sprinkles = input("Add chocolate sprinkles for 30p? (yes/no) ").lower()
if sprinkles == "yes":
    sprinkles_cost = 0.30
else:
    sprinkles_cost = 0.00

# Ask if they want strawberry coulis
coulis = input("Add strawberry coulis for 60p? (yes/no) ").lower()
if coulis == "yes":
    coulis_cost = 0.60
else:
    coulis_cost = 0.00

# Calculate the total cost
total_cost = serving_cost + scoops_cost + flake_cost + sprinkles_cost + coulis_cost

# Show the total cost
print(f"Total cost: £{total_cost:.2f}")
