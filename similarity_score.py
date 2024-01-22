# Input hobbies for two people
person1_hobbies = input("Person 1: Please enter hobbies, separated by spaces: ").lower().split()
person2_hobbies = input("Person 2: Please enter hobbies, separated by spaces: ").lower().split()
# Calculate similarity score without using set
common_hobbies = [hobby for hobby in person1_hobbies if hobby in person2_hobbies]
similarity_score = 0
# Count the number of common hobbies without using len
for _ in common_hobbies:
    similarity_score += 1
# Print the result
print(f"\nYou have {similarity_score} hobbies in common!")