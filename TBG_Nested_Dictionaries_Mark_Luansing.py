# TBG Nested Dictionaries - Mark Luansing
# May 6th, 2022

# This code prints descriptions about characters,
# items, and locations using dictionaries. Uses
# loops to print the statements.

"""Characters and Traits"""
print("\033[1m" + "Meet The Crew:" + "\033[0m")

characters = {
    'Gadgetsmith': {
        'first': 'Betty',
        'last': 'Blitz',
        'trait': 'good at making gadgets. Invented time and space itself.',},
    'Ghostrider': {
        'first': 'Jean',
        'last': 'Paul',
        'trait': 'the fastest driver known to exist.',},
    'H4CK3RM4N': {
        'first': 'Harry',
        'last': 'Hackerman',
        'trait': 'a boy genius, very good at hacking.',},
    'Jim': {
        'first': '[REDACTED]',
        'last': '[REDACTED]',
        'trait': 'reliable',},
    }

for title, user_info in characters.items():
    print(f"\nNickname: {title}")
    full_name = f"{user_info['first']} {user_info['last']}"
    trait = user_info['trait']
    
    print(f"Full name: {full_name}")
    print(f"Trait: Is {trait}")

"""Gadget Traits"""
print("\n\033[1m" + "The Gadgets: Which two will you pick?" + "\033[0m")

gadgets = {
    'Exothermic Charge':
    {'desc': 'Uses heat to create holes in even the thickest of steel'},
    'Drone':
    {'desc': 'A small drone, could possibly fit in small spaces'},
    'Smoke Bomb':
    {'desc': 'Grants cover from any angle'},
    'Tripwire':
    {'desc': "Can be used to make sure you're not being followed"},
    'Banana':
    {'desc': 'A tasty snack?'},
    'Crowbar':
    {'desc': 'Can be used to pry open very secure glass cases'},
    }

for gadget_name, item_desc in gadgets.items():
    print(f"\n{gadget_name} | ")
    desc = item_desc['desc']
    print(f"Usage: {desc}")

"""Location Traits"""
print("\n\033[1m" + "The Bank and Entrances" + "\033[0m")

entrances = {
    'The Citadel':
    {'location_desc':
     'The largest and most secure bank in the world. The home of our hopes and dreams.',
    'direction': 'Located in the centre of the city'},
    'Front Entrance':
    {'location_desc': "Easiest way to get in, but there's tons of risk to it.",
     'direction': 'South side of the building'},
    'Back Entrance':
    {'location_desc': 'Not the safest, but can save us some precious time.',
     'direction': 'Top of the building'},
    'Skylight':
    {'location_desc': 'May be hard to get into without the right tools, but its the safest.',
     'direction': 'East side of the building'},
    }

for entrance, location_desc in entrances.items():
    direction = location_desc['direction']
    print(f"\n{entrance} | {direction} ")
    desc = location_desc['location_desc']
    print("\033[1m" + "Jim: " + "\033[0m" f"{desc}")