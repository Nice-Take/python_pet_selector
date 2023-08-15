import pet_options
import util
import family_profile
import time

util.welcome()

if util.ready_check():
    # Init list to add family member objects to for later calculations
    family_members = []

    # Create person object to store the preference of each memeber of the family from user input
    # Each of these steps requires validation upon initial input so we don't encounter an error during calculation
    for person in range(util.set_family_size()):

        # Begin taking and validation of user input
        choice_weight = util.validate_int(f"What is Person #{person+1}'s preference weight? (1-10): ")
        mammal_v_reptile = util.validate_exact_str(f"Does Person #{person+1} prefer", "mammal", "reptile")
        cuddle_v_spectate = util.validate_exact_str(f"Does Person #{person+1} prefer to", "cuddle", "spectate")

        # Create an object for each set of input for each person to stay organized and tidy
        person = family_profile.Person(preference_weight = choice_weight,
                                       mammal_or_reptile = mammal_v_reptile,
                                       cuddle_or_spectate = cuddle_v_spectate)

        # Add the new person object to a list for later calculations
        family_members.append(person)

    # Calculating the family's weighted preference and unpacking the return list into (2) corresponding variables
    fam_mammal_v_reptile, fam_cuddle_v_spectate = (util.calculate_family_preferences(family_members))
    
    # Requesting the remaining necessary family situation information, the per-person input is compelete at this point
    dander_allergy = util.validate_y_n("Is anyone in the family allergic to pet dander? (Y/N): ")
    noise_restrictions = util.validate_y_n("Are there noise restrictions where you live? (Y/N): ")
    yard = util.validate_y_n("Does your family have a yard? (Y/N): ")
    budget = util.validate_int("What is your annual pet budget? (USD): ")
    days_absent = util.validate_int("How many days at a time will you be away?: ")

    # Create family_profile.Family object from the obtained information
    fam_profile = family_profile.Family(family_size=len(family_members),
                                    dander_allergies = dander_allergy,
                                    noise_restriction = noise_restrictions,
                                    annual_budget = budget,
                                    consecutive_days_away = days_absent,
                                    has_yard = yard,
                                    mammal_or_reptile = fam_mammal_v_reptile,
                                    cuddle_or_spectate = fam_cuddle_v_spectate)

# Matching the best fit pet to the family's specifications
selected_pet = util.match_family_to_pet(fam_profile, pet_options.all_possible_pets)

# Getting the name of the selected pet for presentation to the user
new_pet = selected_pet.name

# Present the user with the result with timing to help build excitement
print(f"Thank you for using the Pet Selector!\nSit tight while we calculte your pet...")
time.sleep(1)
print(f"Hmmmm.....")
time.sleep(.75)
print("I've got it!")
time.sleep(.5)
print(f"\nThe best pet for your family is a...")
time.sleep(.75)
print(f"\n     -----  [{new_pet.capitalize()}]  -----     \n")
time.sleep(2)
print("""Thank you and we hope we have helped
    bring clarity to your decision!\n 
      ----- Bye! -----\n""")