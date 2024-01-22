
# Chatbot
# Author: Brant
# Date: 7 November 2023

# Greet the user
print("Hello welcome to Mcdonald's")

# Ask the user
eat = input("Did you eat?").lower()
study = input("Did you study?").lower()
laundry = input("Did you do your laundry?").lower()
grandma = input("Did you call your grandma?").lower()

# Store their answers
total_price = 0

if eat == "yes":
    total_point += 1
else print("THEN GO EAT YOUR FOOD!")

if study == "yes":
    total_point += 1
else print("THEN GO EAT YOUR FOOD!")

if laundry == "yes":
    total_point += 1
 else print("THEN GO EAT YOUR FOOD!")

if grandma == "yes":
    total_point += 1
else print("THEN GO EAT YOUR FOOD!")


# Calculations

print("Total price:", total_point)

# With tax
tax_rate = 0.14
total_with_tax = total_price * (1 + tax_rate)

# Now, round the total including tax to 2 decimal places and print it
rounded_total_with_tax = round(total_with_tax, 2)
print("Your total with tax comes to: $", rounded_total_with_tax)