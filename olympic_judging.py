# Chatbot
# Author: Brant
# Date: 3 November 2023
# How old are you in 2049

# Greet the user
print("Please answer the following questions based on the NBA Zion Williamson's dunk from 1 to 5.")

# Create a list of questions to ask
questions = [
    "How high was the vertical jump from a scale 1 to 10? 1 is very low, and 10 is very high.",
    "How would you rate the timing from 1 to 10? 10 is excellent timing. 1 is the worst.",
    "From 1 to 10, how would you rate the hand size and control? 10 is excellent ball control, and 1 is the ball slipped away.",
    "How would you rate the speed and approach? 1 slipped before dunk, and 10 is a powerful approach.",
    "How would you rate the strength from 1 to 10? 10 is a powerful dunk. 1 when you assume that he can be blocked by you.",
    "From 1 to 10, how would you rate the body control? 10 is excellent body control, and 1 is he fell on landing",
    "Rate the creativity of the dunk from 1 to 10, where 10 is highly creative and 1 is not creative at all.",
    "How confident did the player seem during the dunk? Rate from 1 to 10, where 10 is extremely confident and 1 is not confident.",
    "From a technical standpoint, rate the dunk from 1 to 10. Consider hand placement, arm extension, and wrist manipulation.",
    "What was the impact of the dunk? Rate from 1 to 10, where 10 is highly impactful and intimidating, and 1 is no impact at all."
]


final_score = 0

# Ask the questions to the user
for question in questions:
    print(question)
    
    # Store their response
    rating = int(input().strip(",.?! "))
    final_score += rating

# Do some math - average
average_score = final_score / len(questions)

# Present the results to the user
print(f"The average score of this chip is: {average_score:.2f} / 5")