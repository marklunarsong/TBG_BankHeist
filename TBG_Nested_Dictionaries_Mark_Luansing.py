# TBG Nested Dictionaries - Mark Luansing
# May 6th, 2022

# This code prints descriptions about characters,
# items, and locations using dictionaries. Uses
# loops to print the statements.

"""Characters and Traits"""
print("\033[1m" + "Meet The Crew:" + "\033[0m")                                                      # Prints title for the crew dictionary

characters = {                                                                                       # Creates nested dictionary for character and traits
    'Gadgetsmith': {                                                                                 # Creates data set for Gadgetsmith's key-pair values
        'first': 'Betty',
        'last': 'Blitz',
        'trait': 'good at making gadgets. Invented time and space itself.',},      
    'Ghostrider': {                                                                                  # Creates data set for Ghostriders's key-pair values
        'first': 'Jean',
        'last': 'Paul',
        'trait': 'the fastest driver known to exist.',},
    'H4CK3RM4N': {                                                                                   # Creates data set for H4CK3RM4N's key-pair values
        'first': 'Harry',
        'last': 'Hackerman',
        'trait': 'a boy genius, very good at hacking.',},
    'Jim': {                                                                                         # Creates data set for Jim's key-pair values
        'first': '[REDACTED]',
        'last': '[REDACTED]',
        'trait': 'reliable',},
    }

for title, user_info in characters.items():                                                          # Creates loop for printing characters and their traits
    print(f"\nNickname: {title}")                                                                    # Prints title for the character nicknames
    full_name = f"{user_info['first']} {user_info['last']}"                                          # Creates a variable for the full name using an f-string
    trait = user_info['trait']                                                                       # Creates a variable for character traits
    
    print(f"Full name: {full_name}")                                                                 # Prints full name of character using the variable
    print(f"Trait: Is {trait}")                                                                      # Prints character's trait using the variable

"""Gadget Traits"""
print("\n\033[1m" + "The Gadgets: Which two will you pick?" + "\033[0m")

gadgets = {                                                                                          # Creates dictionary for gadgets and descriptions
    'Exothermic Charge':                                                                             # Creates data set for Exothermic Charge and it's description 
    {'desc': 'Uses heat to create holes in even the thickest of steel'},
    'Drone':                                                                                         # Creates data set for the Drone and it's description 
    {'desc': 'A small drone, could possibly fit in small spaces'},
    'Smoke Bomb':                                                                                    # Creates data set for the Smoke Bomb and it's description 
    {'desc': 'Grants cover from any angle'},
    'Tripwire':                                                                                      # Creates data set for Tripwire and it's description 
    {'desc': "Can be used to make sure you're not being followed"},
    'Banana':                                                                                        # Creates data set for Banana and it's description 
    {'desc': 'A tasty snack?'},
    'Crowbar':                                                                                       # Creates data set for Crowbar and it's description 
    {'desc': 'Can be used to pry open very secure glass cases'},
    }

for gadget_name, item_desc in gadgets.items():                                                       # Creates loop for printing the gadgets and their traits
    print(f"\n{gadget_name} | ")                                                                     # Prints title for the gadget
    desc = item_desc['desc']                                                                         # Creates a variable for the description
    print(f"Usage: {desc}")                                                                          # Prints the description using the variable

"""Location Traits"""
print("\n\033[1m" + "The Bank and Entrances:" + "\033[0m")                                           # Prints title for the locations/entrances of the TBG

entrances = {                                                                                        # Creates dictionary for locations and descriptions
    'The Citadel':                                                                                   # Creates data set for the bank and its description
    {'locat_desc':
     'The largest and most secure bank in the world. The home of our hopes and dreams.',
    'direction': 'Located in the centre of the city'},
    'Front Entrance':                                                                                # Creates data set for the front entrance and its description
    {'locat_desc': "Easiest way to get in, but there's tons of risk to it.",
     'direction': 'South side of the building'},
    'Back Entrance':                                                                                 # Creates data set for the back entrance and its description
    {'locat_desc': 'Not the safest, but can save us some precious time.',
     'direction': 'Top of the building'},
    'Skylight':                                                                                      # Creates data set for the skylight and its description
    {'locat_desc': 'May be hard to get into without the right tools, but its the safest.',  
     'direction': 'East side of the building'},
    }

for entrance, locat_desc in entrances.items():                                                       # Creates loop for printing the locations and descriptions
    direction = locat_desc['direction']                                                              # Creates variable for direction of the location
    print(f"\n{entrance} | {direction} ")                                                            # Prints the location name with the direction
    desc = locat_desc['locat_desc']                                                                  # Creates a variable for the location description
    print("\033[1m" + "Jim: " + "\033[0m" f"{desc}")                                                 # Prints dialogue with a statement about the location (uses variable)
