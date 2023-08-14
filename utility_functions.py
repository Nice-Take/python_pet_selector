import time
import typing
import family_profile

def welcome() -> None:
    """ 
        Prints a welcome message notifying the user that the 
        program has begun. Also prints a description of the
        expected process and what the result will be.
    """
    welcome_msg = "Hello and welcome to the Pet Selector!"
    program_brief_msg = "Answer a few questions to find your best fit pet!"
    print(welcome_msg)
    time.sleep(1)
    print(program_brief_msg)
    time.sleep(1)


def ready_check() -> bool:
    """
        Verifying that the user is ready to run the program. 
        Anything other than input 'Y' or 'y' will return False.
    """
    begin = input("Are you ready to begin? (Y/N): ")
    if begin.upper() == 'Y':
        print("Here we go!\n")
        return True
    else:
        print("You have indicated you are not ready to proceed.")
        return False


def set_family_size() -> int:
    """
    Retrieves and validates the user's input family size as an int.
    If anything other than an integer is returned, the user will
    be asked to try again until an integer is successfully entered.
    """
    validating = True
    while validating == True:
        family_size = input("How many people are in your same-house family?: ")
        # Handling any accidental spaces entered
        family_size.replace(" ", "")

        # Validating input as numeric
        if family_size.isdigit():
            validated_family_size = int(family_size)
            # Input has been validated, end loop and return
            validating = False
        else:
            # Provide error message to the user and reattempt
            print("Oops!\nPlease enter a valid whole number. ")
    return validated_family_size


def calculate_family_preferences(family_members: list) -> list:
    """
    Takes in a list of family_profile.Person objects, then calculates
    the and returns a list of strings containing the corresponding 
    value with the highest weighted matching score. This result will 
    set the family's preference for - mammal vs reptile - & - cuddle vs
    spectate.

    Mammal vs reptile result is item at index 0

    Cuddle vs spectate result is item at index 1
    """

    # Init neutral scores for decision categoires
    mammal_score = 0
    reptile_score = 0
    cuddle_score = 0
    spectate_score = 0

    for member in family_members:
        weight_multiplier = member.preference_weight

        if member.mammal_or_reptile == 'mammal':
            mammal_score += 10 * weight_multiplier
        else:
            reptile_score += 10 * weight_multiplier
        
        if member.cuddle_or_spectate == 'cuddle':
            cuddle_score += 10 * weight_multiplier
        else:
            spectate_score += 10 * weight_multiplier

    if mammal_score >= reptile_score:
        mammal_vs_reptile_choice = 'mammal'
    else:
        mammal_vs_reptile_choice = 'reptile'

    if cuddle_score >= spectate_score:
        cuddle_vs_spectate_choice = 'cuddle'
    else:
        cuddle_vs_spectate_choice = 'spectate'

    family_preferences = [mammal_vs_reptile_choice, cuddle_vs_spectate_choice]
    return family_preferences


def match_family_to_pet(family_object: family_profile.Family) -> str:
    """
    Takes in a family object as a single parameter and returns a string of the 
    best-fit pet for the particular family.
    """