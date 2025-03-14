"""CSC111 Project 1: Text Adventure Game

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""

# Note: You may add in other import statements here as needed
from game_data import World, Item, Location, Player
import sys


# Note: You may add helper functions, classes, etc. here as needed

# Note: You may modify the code below as needed; the following starter template are just suggestions

def handle_choice(world, player, locationn, choicee):
    """
    Handles the player's choice and updates the game state accordingly.
    """
    if choicee == "look":
        print(locationn.full_description)
    elif choicee == "inventory":
        player.display_inventory()
    elif choicee == "score":
        print(p.moves)
    elif choicee == "quit":
        sys.exit("Goodbye!")


def handle_go_direction(ww, pp):
    """
     This handles the go direction, which moves the player in the specified direction either to the north, south,
     east, or west.
    """
    if choice.startswith("go") and len(choice) >= 4:
        direction = choice[3:]
        # p.move(direction)
        if ww.get_location(pp.x, pp.y).location_number == -1:
            print("That way is blocked.")
            pp.reverse_move(direction)
        else:
            if direction == 'north':
                pp.y += 1
            elif direction == 'south' and pp.y >= 0:
                pp.y -= 1
            elif direction == 'east':
                pp.x += 1
            elif direction == 'west' and pp.x >= 0:
                pp.x -= 1
            pp.moves -= 1
            if pp.moves == 0:
                sys.exit("You have lost the game")


def take_item(itemm: str, locationn: Location):
    """
        Adds an item to the player's inventory.
        """
    item = itemm[5:]
    if item in locationn.available_items:
        for item2 in w.load_items(w.items):
            if item2.name == item:
                locationn.available_items.remove(item2)
        p.inventory.append(item)
        print(f"You have taken the {item}")
    else:
        print("You cannot take that item")


def drop_item(itemm: str, locationn):
    """
    This function removes an item from the player's inventory and drops it at the current location.

    """
    itemm = itemm[5:]
    if itemm in p.inventory:
        p.inventory.remove(itemm)
        locationn.available_items.append(itemm)
        print(f"You have dropped the {itemm}")
    else:
        print("This item isn't in your inventory")


if __name__ == "__main__":
    w = World(open("map.txt"), open("locations.txt"), open("items.txt"))
    p = Player(0, 0)  # set starting location of player; you may change the x, y coordinates here as appropriate
    # i = Item("", 0, 0, 0)
    # l = Location("", "", "", "", 0, [], 0, p.x, p.y)
    # t_card = Item('t_card', 3, 13, 0)
    # pen = Item('pen', 10, 13, 0)
    # cheat_sheet = Item('pen', 11, 13, 0)

    menu = ["look", "inventory", "score", "quit"]
    while not p.victory:
        location = w.get_location(p.x, p.y)
        if not location.has_been_visited:
            print(location.full_description)
            location.has_been_visited = True
        else:
            print(location.brief_description)

        # Depending on whether it's been visited before,
        # print either full description (first time visit) or brief description (every subsequent visit)

        print("What to do? \n")
        print("[menu]")
        for action in location.available_actions():
            print(action)
        if p.inventory:
            inventory_options_list = []
            for item in p.inventory:
                action1 = "drop " + item.name
                inventory_options_list.append(action1)
            print(inventory_options_list)
        choice = input("\nEnter action: ")

        if choice == "[menu]":
            print("Menu Options: \n")
            for option in menu:
                print(option)
            choice = input("\nChoose action: ")
            choice = choice.lower()
            handle_choice(w, p, location, choice)

        if choice.startswith("go"):
            handle_go_direction(w, p)

        elif choice.startswith("take"):
            take_item(choice, location)

        elif choice.startswith("drop"):
            drop_item(choice, location)

        if w.get_location_coordinates(13):
            required_items = ['t_card', 'pen', 'cheat_sheet']
            items_in_location = [item.name for item in location.available_items]
            for item_name in required_items:
                if item_name not in items_in_location:
                    pass
                else:
                    p.victory = True

        # TODO: CALL A FUNCTION HERE TO HANDLE WHAT HAPPENS UPON THE PLAYER'S CHOICE
        #  REMEMBER: the location = w.get_location(p.x, p.y) at the top of this loop will update the location if
        #  the choice the player made was just a movement, so only updating player's position is enough to change the
        #  location to the next appropriate location
        #  Possibilities:
        #  A helper function such as do_action(w, p, location, choice)
        #  OR A method in World class w.do_action(p, location, choice)
        #  OR Check what type of action it is, then modify only player or location accordingly
        #  OR Method in Player class for move or updating inventory
        #  OR Method in Location class for updating location item info, or other location data etc....
