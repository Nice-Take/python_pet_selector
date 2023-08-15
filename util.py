import time
import typing
import family_profile
import pet_options

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
        print("You have indicated you are not ready to proceed.\nProgram Ended.")
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

    # Assigning points for mammal/reptile & cuddle/spectate using weighted user input values
    # To determine the families overall weighted preference
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

    # Compare scores and set result for mammal/reptile
    if mammal_score >= reptile_score:
        mammal_vs_reptile_choice = 'mammal'
    else:
        mammal_vs_reptile_choice = 'reptile'

    # Compare scores and set result for cuddle/spectate
    if cuddle_score >= spectate_score:
        cuddle_vs_spectate_choice = 'cuddle'
    else:
        cuddle_vs_spectate_choice = 'spectate'

    family_preferences = [mammal_vs_reptile_choice, cuddle_vs_spectate_choice]
    return family_preferences


def validate_y_n(prompt: str) -> bool:
    """
    This function wraps the standard input() with measures to validate the user's
    entry and convert it to a boolean.
    """
    raw_input = input(prompt)
    # Removing accidental space from input
    raw_input.replace(" ", "")
    validating = True
    validated_output = bool
    while validating:
        if raw_input.lower() == 'y':
            validated_output = True
            validating = False
        elif raw_input.lower() == 'n':
            validated_output = False
            validating = False
        else:
            raw_input = input("Enter 'Y' for YES or 'N' for NO: ")
    return validated_output


def validate_int(prompt: str) -> int:
    """
    This function wraps the standard input() with validation checks.
    """
    raw_input = clean_str_for_int_conversion(input(prompt))
    validating = True
    validated_output = int
    while validating:
        try:
            validated_output = int(raw_input)
            validating = False
        except:
            raw_input = clean_str_for_int_conversion(input("Please enter only a valid number: "))
    return validated_output


def clean_str_for_int_conversion(input: str) -> str:
    """
    Cleans the string parameter input of symbols commonly entered by users for USD value.
    Examples: '$', '.', ',', ' ' |  
    If a '.' is removed it was likely intended as a decimal and has meaning
    so we round the int instead of replace '.'
    """
    # Removing space from int input
    cleaned = input.replace(" ", "")
    # Removing dollar-sign from user input
    cleaned = cleaned.replace("$", "")
    # Removing commas from user input
    cleaned = cleaned.replace(",", "")
    # Removing periods
    try: 
        cleaned = int(round(cleaned))
        cleaned = str(cleaned)
    except:
        cleaned = cleaned.replace(".", "")
    return cleaned


def validate_exact_str(question_phrase: str, string1: str, string2: str) -> str:
    """
    Takes 3 parameters. First is the phrase at the beginning of the prompt.
    Next is the first string option 'string1' and third is the last 'string2' 
    option that the function user would like input from. The case entered
    is not relevant as this function forces everything to lower before comparing.
    """
    raw_input = input(f"{question_phrase} ({string1} or {string2})?: ")
    validated_output = str
    validating = True
    while validating:
        # Matching input to valid results and returning only once matched
        if raw_input.lower() == string1.lower():
            validated_output = string1.lower()
            validating = False
        elif raw_input.lower() == string2.lower():
            validated_output = string2.lower()
            validating = False
        else:
            raw_input = input(f"Please reply with only '{string1}' or '{string2}: ")
    return validated_output

 
def match_family_to_pet(family: family_profile.Family, possible_pets: list[pet_options.Animal]) -> pet_options.Animal:
    """
    Takes in a family object and a list of possible pets as pet_options.Animal objects
    and returns a pet_options.Animal object that best-fits the family_profile.Family.

    Matches are calculated by matching values and assigning points for each match.
    The Animal that has the highest match value score total will be the Animal 
    returned from this function.
    """

    remove_pet_list = [] # This is implemented because the cleaner .remove() was encoutering an error where only 2 items would remove from list

    # Eliminate pets not categorically viable, ie. allergies, yard, noise restrictions
    # These are done outside of the scoring loop to avoid unnecessary iterations through
    # Animals that are not a viable match for the family in any circumstance.

    # First we check for allergies as this is the single factor that will exclude the most pets
    if family.dander_allergies:
        for pet in possible_pets:
            if pet.has_dander:
                remove_pet_list.append(pet)
    # If the pet does not meet noise restriction requirements it is removed here 
    if family.noise_restriction:
        for pet in possible_pets:
            if pet.has_noise and pet not in remove_pet_list:
                remove_pet_list.append(pet)
    # Here we remove any pet that does not meet the yard requirement
    if family.has_yard == False:
        for pet in possible_pets:
            if pet.requires_yard:
                remove_pet_list.append(pet)

    # Create narrowed list for scoring after eliminating animals that absolutely won't work with the family
    viable_pets = []
    for pet in possible_pets:
        if pet in possible_pets and pet not in remove_pet_list:
            viable_pets.append(pet)

    # Begin scoring loop based upon remaining family and pet attributes
    for pet in viable_pets:
        if pet.mammal_or_reptile == family.mammal_or_reptile:
            pet.add_score(10)
        if pet.cuddle_or_spectate == family.cuddle_or_spectate:
            pet.add_score(10)
        if pet.required_budget <= family.annual_budget:
            pet.add_score(8)
        if pet.required_budget >= family.annual_budget:
            pet.subtract_score(-2)
        if pet.days_ok_alone >= family.consecutive_days_away:
            pet.add_score(2)
        else:
            pet.subtract_score(3)

    # Retrieve the pet with the highest score
    best_fit_pet = pet_options.Animal
    highscore = 0
    for pet in viable_pets:
        if pet.score > highscore:
            highscore = pet.score
            best_fit_pet = pet
    # Returing the pet with the highest overall score
    return best_fit_pet
