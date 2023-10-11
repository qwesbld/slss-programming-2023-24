# Chatbot
# Author: Brant
# Date: 20 september 2023

# Greet the user
print("Hello there! ")
print("I'm a crude Chatbot, here to talk with you.")

# Get the user's name and store it in a variable 
user_name = input("So... What's your name? ")

# Respond the user's name in a friendly way
print(f"It's good to meet you, {user_name}.")

# Ask the user what their favourite food is 
favorite_food = input("whats your favorite food? ")

print(favorite_food)
# Make a comment about their food
print(f"OOOOOooooooooOOOoooooooo, {favorite_food} sounds good!")

print("MMMmmMMMmmmmMMM thats delicious")

#if their favorite food is sushi reply with yum
if favorite_food == "sushi" or favorite_food == "Sushi":
    print("Yum! 🍣")
    print("I think I love sushi! ")
elif favorite_food == "burgers" or favorite_food == "Burgers" or favorite_food == "burger" or favorite_food == "Burger":
    print("🍔")
    print("Your american! ")
else:

    # Make a comment about their food but NOT BE  TERRIBLY REPETITIVE
    # Create a list of possible responses 
    list_of_food_responces = [
        f"Oh. I've never had {favorite_food} before.", 
        "Mmmmm, that sounds good!", 
        "I heard that is delicious.", 
        "Cool"
    ]
    # Choose one of those responses randomly 
    import random
    random_food_response = random.choice(list_of_food_responces)

    # Print out that chosen response
    print(random_food_response)
