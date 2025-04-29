def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")
print_greeting()


def check_letter():
    letter = input("enter a letter a-z: ")
    vowels = ["a", "e" , "i", "o", "u"]
    if letter.lower() in vowels:
        print(f"the letter {letter} is a vowel")
    else: 
        print(f"the letter {letter} is a consonant ")
# check_letter()




def check_voting_eligibility():
    age = int(input("please enter your age: "))
    print("you old enough to vote " if age >= 18 else "YOUNG")
# check_voting_eligibility()



def calculate_dog_years():
    dog_age = int(input("how old is ur dog in years : "))
    if dog_age <= 2:
        dog_age = dog_age*10
    else:
        dog_age = (dog_age -2)*7+20
    print(dog_age)
# calculate_dog_years()


# # Exercise 4: Weather Advice
# #
# # Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
# #
# # Requirements:
# # - The script should prompt the user to enter if it is cold (yes/no).
# # - Then, ask if it is raining (yes/no).
# # - Use logical operators to determine clothing advice:
# #   - If it is cold AND raining, print "Wear a waterproof coat."
# #   - If it is cold BUT NOT raining, print "Wear a warm coat."
# #   - If it is NOT cold but raining, print "Carry an umbrella."
# #   - If it is NOT cold AND NOT raining, print "Wear light clothing."
# #
# # Hints:
# # - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    

# Call the function
weather_advice()


# # Exercise 5: What's the Season?
# #
# # Write a Python function named `determine_season` that figures out the season based on the entered date.
# #
# # Requirements:
# # - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# # - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# # - Determine the current season based on the date:
# #      - Dec 21 - Mar 19: Winter
# #      - Mar 20 - Jun 20: Spring
# #      - Jun 21 - Sep 21: Summer
# #      - Sep 22 - Dec 20: Fall
# # - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
# #
# # Hints:
# # - Use 'in' to check if a string is in a list or tuple.
# # - Adjust the season based on the day of the month when needed.
# # - Ensure to validate input formats and handle unexpected inputs gracefully.

# def determine_season():
#     # Your control flow logic goes here

# # Call the function
# determine_season()
