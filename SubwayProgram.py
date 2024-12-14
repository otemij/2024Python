# Write your code here :-)
print("This is a subway menu made by Jimeto Onyeabo")
print("")



finalTotal = 0.00  # Corrected initialization of finalTotal

# Get size of the sandwich
size = int(input("Enter in the size of your sandwich 6 inches or 12: "))
sizeCost = 0

if size == 6:
    sizeCost = 1.65
elif size == 12:
    sizeCost = 2.05

# Get bread type
print("Enter in which bread type you want. Plain, Wheat, Italian or Cheese and Herbs. Type in P for Plain, W for wheat, I for italian and C for cheese and herbs.")
breadType = input("Enter in your bread type:")
breadCost = 0.00

if breadType == "P" or breadType == "p":
    breadCost = 0.4
elif breadType == "W" or breadType == "w":
    breadCost = 0.65
elif breadType == "I" or breadType == "i":
    breadCost = 0.75
elif breadType == "C" or breadType == "c":
    breadCost = 0.8  # Corrected the assignment here
else:
    print("Please select one of the options")

# Get fillings type
print("The filling types are : Cheese and Tomato (75p), Italian Bacon and Peperoni (1.10), Tuna and Mayo (0.95), Turkey and Ham (1.35), Chicken Teriyaki (1.40), and Steak and Cheese (1.95)")
print("For Cheese and Tomato, enter in 1. For Italian Bacon and Peperoni, enter in 2. For Tuna and Mayo, enter in 3. For Turkey and Ham, enter in 4. For Chicken Teriyaki, enter in 5. For Steak and Cheese, enter in 6.")
fillings = int(input("Enter the number corresponding to your choice of filling: "))  # Convert input to integer
fillingsCost = 0.0

if fillings == 1:
    fillingsCost = 0.75
elif fillings == 2:
    fillingsCost = 1.10
elif fillings == 3:
    fillingsCost = 0.95
elif fillings == 4:
    fillingsCost = 1.35
elif fillings == 5:
    fillingsCost = 1.40
elif fillings == 6:
    fillingsCost = 1.95
else:
    print("You did not enter one of the options")
finalTotal = sizeCost + breadCost + fillingsCost
eatIn = input("Are you eating in: ")
if eatIn == "Yes" or eatIn == "yes":
    finalTotal = finalTotal * 1.05
elif eatIn == "No" or "no":
    finalTotal = finalTotal
else:
    print("You did not enter in the right one")

print(f"Your final total is £{finalTotal}")