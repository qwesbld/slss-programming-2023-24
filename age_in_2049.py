# Chatbot
# Author: Brant
# Date: 3 November 2023
# How old are you in 2049

# Greet the user
print("Would you like to know your age in 2049?")

# Age to ask
current_age = input("How old are you? ")

# Calculate the number of years until 2049
years_until_2049 = 2049 - 2023  # Replace 2023 with the current year if needed

# Do some math
# Convert current_age to an integer before addition
age_in_2049 = years_until_2049 + int(current_age)

# Present the results to the user
print(f"Your age will be {age_in_2049} in 2049.")

print("This code was made in 2023")