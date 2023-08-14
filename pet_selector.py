import pet_options
import utility_functions
import family_profile


# console_interaction.welcome()

if utility_functions.ready_check() == True:
    # print(console_interaction.set_family_size())

    # Init list to add family member objects to for later calculations
    family_members = []

    # Create Person object for each member of the family from user input
    for person in range(utility_functions.set_family_size()):
        person_choice_weight = input(f"What is Person #{person+1}'s preference weight?: ") # validate int
        pref_m_or_r = input(f"Does Person #{person+1} prefer mammal or reptile?: ") # validate entry
        pref_c_or_s = input(f"Does Person #{person+1} prefer to cuddle or spectate animals?: ") # validate entry
        # Create object for each person's entry
        person = family_profile.Person(preference_weight = int(person_choice_weight),
                                       mammal_or_reptile= pref_m_or_r,
                                       cuddle_or_spectate= pref_c_or_s)
        # Add the new object to a list for later calculation
        family_members.append(person)

    # Unpacking the calculate family preference return list
    family_mammal_vs_reptile_choice, family_cuddle_vs_spectate_choice = (utility_functions.calculate_family_preferences(family_members))
    
    # Request the remaining necessary user input
    pet_dander = input("Is anyone in the family allergic to pet dander?: ")
    noise_restrictions = input("Do you have any noise restrictions where you live?: ")
    pet_budget = input("What is your annual pet budget?: ")
    days_absent = input("How many days at a time will you be away?")
    has_yard = input("Do you have a yard?: ")

    # Create family_profile.Family object from the obtained information
    profile = family_profile.Family(family_size=len(family_members),
                                    dander_allergies=pet_dander,
                                    noise_restriction=noise_restrictions,
                                    annual_budget=pet_budget,
                                    consecutive_days_away=days_absent,
                                    have_yard=has_yard,
                                    fam_avg_mammal_or_reptile=family_mammal_vs_reptile_choice,
                                    fam_avg_cuddle_or_spectate=family_cuddle_vs_spectate_choice)

    print(utility_functions.find_matching_pet())