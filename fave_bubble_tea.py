# bubble tea popularity algorithm
# Brant
# 2023-10-26

# Ask 5 users what their favourite bubble tea place is
# Prints out a summary of the data

# ------ CONSTANTS 

NUM_RESPONDENTS = 5

# ------

# Like counters
coco_likes = 0      # Initialize the variable to 0
suntea_likes = 0
chatime_likes = 0
bubqueen_likes = 0
unknownvotes = 0

for _ in range(NUM_RESPONDENTS):
    # Ask the user what their favourite place is
    print("What's your favourite bubble tea place?")
    fave_place = input().strip(",.?! ").lower()

    # Tally or counting algo
    if fave_place == "coco":
        coco_likes = coco_likes + 1
    elif fave_place == "suntea":
        suntea_likes += 1       # alternate to above
    elif fave_place == "chatime":
        chatime_likes += 1
    elif fave_place == "bubble queen":
        bubqueen_likes += 1
    else:
        unknownvotes += 1

# Print out a summary
print(" ")
print("Summary")
print("=======")
print(f"Coco: {coco_likes} votes |  {coco_likes / NUM_RESPONDENTS * 100}%")
print(f"SunTea: {suntea_likes} votes |  {suntea_likes / NUM_RESPONDENTS * 100}%")
print(f"Chatime: {chatime_likes} votes |  {chatime_likes / NUM_RESPONDENTS * 100}%")
print(f"Bubble Queen: {bubqueen_likes} votes |  {bubqueen_likes / NUM_RESPONDENTS * 100}%")
print(f"Unknown votes: {unknownvotes} votes |  {unknownvotes / NUM_RESPONDENTS * 100}%")