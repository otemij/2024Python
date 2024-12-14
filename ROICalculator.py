# Ask the user to input the total amount spent (Total Costs)
total_costs = float(input("Enter the total amount spent/invested on the business: "))

# Ask the user to input the total amount raised (Total Sales)
total_sales = float(input("Enter the total amount raised by the business: "))

# Calculate the profit or loss
profit_or_loss = total_sales - total_costs

# Check if the business made a profit or a loss
if profit_or_loss > 0:
    print("The business made a profit of", profit_or_loss)
elif profit_or_loss < 0:
    print("The business made a loss of", abs(profit_or_loss))
else:
    print("The business broke even.")

# Calculate the Return on Investment (ROI)
if total_costs != 0:
    roi = (profit_or_loss / total_costs) * 100
    print("The Return on Investment (ROI) is:", roi, "%")
else:
    print("ROI cannot be calculated because the total costs are 0.")
