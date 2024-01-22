
# Chatbot
# Author: Brant
# Date: 7 November 2023

# Greet the user
print("Hello welcome to Mcdonald's")

# Ask the user
burger = input("Would you like to buy a burger for $5? (Yes/No)").lower()
fries = input("Would you like to buy fries for $3? (Yes/No)").lower()
soda = input ("Would you like to buy a soda for $1.5? (Yes/No)").lower()

# Store their answers
total_price = 0

if burger == "yes":
    total_price += 5

if fries == "yes":
    total_price += 3

if soda == "yes":
    total_price += 1.5

# Calculations

print("Total price:", total_price)

# With tax
tax_rate = 0.14
total_with_tax = total_price * (1 + tax_rate)

# Now, round the total including tax to 2 decimal places and print it
rounded_total_with_tax = round(total_with_tax, 2)
print("Your total with tax comes to: $", rounded_total_with_tax)