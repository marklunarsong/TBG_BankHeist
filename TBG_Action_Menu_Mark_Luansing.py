# TBG Action Menu - Mark Luansing
# May 13th, 2022

# This code creates an action menu
# for the TBG Bank Heist introduction

def ask_name():
    name = input("Tell me your name: ")
    print("""\nIt is the middle of the night and you are by the docks.
You see in front of you multiple warehouses""")
    print(f"Unknown Voice: Hello {name}, I have a job for you.")
    print("Unknown Voice: So please, enter the red warehouse right infront of you.\n")

def intro_scene():
    print("""Which colour warehouse will you enter?""")
    print("""> Enter the Red Warehouse?
> Enter the Blue Warehouse?
> Enter the Green Warehouse?""")
    warehouse_choice = input()
    
    if warehouse_choice == "red":
        print("You enter the red warehouse.")
        scene_2()
    elif warehouse_choice == "blue":
        print("You enter the blue warehouse.")
        scene_2()
    elif warehouse_choice == "green":
        print("You enter the green warehouse.")
        scene_2()
    else:
        print("\nInvalid input. Try again.")
        intro_scene()
        
def reask_scene_2():
    print("""Do you want to keep inspecting more gadgets?""")
    yes_no_scene_2 = input()
    
    if yes_no_scene_2 == "yes":
        scene_2()
    elif yes_no_scene_2 == "no":
        print("You look to the whiteboard and see a blueprint.")
        
        
def scene_2():
    print("""You see a group of people around a table.
On the table you see a set of gadgets and tools.""")
    print("""\nWhich gadget do you inspect?
> Drone
> Grappling hook
> Smoke Bomb
> Exothermic Charge
> Tripwire
> Banana
> Crowbar""")
    gadget_choice = input()
    
    if gadget_choice == "drone":
        print("""A small metal drone with two blades to allow lift.
It seems small enough to fit into tight spaces...""")
        reask_scene_2()
    elif gadget_choice == "grappling hook":
        print("""A rope attached to a metal hook.""")
        reask_scene_2()
    elif gadget_choice == "smoke bomb":
        print("""A smoke bomb, can cover a large area """)
        reask_scene_2()
    elif gadget_choice == "exothermic charge":
        print("""A breaching charge that can melt through metal""")
        reask_scene_2()
    elif gadget_choice == "tripwire":
        print("""A tripwire that can help watch your back""")
        reask_scene_2()
    elif gadget_choice == "banana":
        print("""A regular banana""")
        reask_scene_2()
    elif gadget_choice == "crowbar":
        print("""A regular crowbar. May be able to open cases""")
        reask_scene_2()
    else:
        print("\nInvalid input. Try again.")
        reask_scene_2()

ask_name()
intro_scene()

    
    
