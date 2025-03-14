"""CSC111 Project 1: Text Adventure Game Classes

Instructions (READ THIS FIRST!)
===============================

This Python module contains the main classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""
from typing import List, Optional, TextIO, Tuple


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - name:
            The string name assigned to each loaction.
        - full_description:
            The first description given for any location. It is only given once, automatically.
        - brief_description:
            The description of a location given upon each subsequent visit to a location. It contains only the key
            information which the player most needs to know.
        - examine:
            Provides a closer look at the location.
        - location_number
            The number used to identify each location on the game map.
        - position:
            The player's geographical location on the game-map grid.
        - available_items:
            The items which are available for the player to interact with.
        - has_been_visited:
            Whether the location has already been visited by the player.
        - points
            [no value yet. a place-holder for future use]


    Representation Invariants:
        - full_description != ''
        - brief_description != ''
        - examine != ''
        - isinstance(location_number, int)
        - location_number > 0
        - position[0] >= 0 and position[1] >= 0
    """

    def __init__(self, name: str, full_description: str, brief_description: str, examine: str, location_number: int,
                 available_items: List['Item'], points: int, x: int, y: int) -> None:
        """Initialize a new location.
        """

        # NOTES:
        # Data that could be associated with each Location object:
        # a position in the world map,
        # a brief description,
        # a long description,
        # a list of available commands/directions to move,
        # items that are available in the location,
        # and whether the location has been visited before.
        # Store these as you see fit, using appropriate data types.
        #
        # This is just a suggested starter class for Location.
        # You may change/add parameters and the data available for each Location object as you see fit.
        #
        # The only thing you must NOT change is the name of this class: Location.
        # All locations in your game MUST be represented as an instance of this class.

        self.name = name
        self.full_description = full_description
        self.brief_description = brief_description
        self.examine = examine
        self.location_number = location_number
        self.position = (x, y)
        self.available_items = available_items
        self.has_been_visited = False
        self.points = points

    def available_actions(self) -> list:
        """
        Return the available actions in this location.
        The actions should depend on the items available in the location
        and the x,y position of this location on the world map.
        """

        # NOTE: This is just a suggested method
        # i.e. You may remove/modify/rename this as you like, and complete the
        # function header (e.g. add in parameters, complete the type contract) as needed

        player_options_list = ["examine location"]

        for item in self.available_items:
            action1 = "take " + item.name

            player_options_list.append(action1)

        movement_options = ["north", "south", "east", "west"]
        for movement in movement_options:
            movement_comand = "go " + movement
            player_options_list.append(movement_comand)

        return player_options_list


class Item:
    """An item in our text adventure game world.


    Instance Attributes:
        - name:
            The name of the item in question.
        - description:
            A short description of the object
        - start_position:
            The location on the map where the item starts the game
        - target_position:
            The location on the map where the item should idealy be at the end of a game
        - target_points:
            The amount of points you can obtain for each item


    Private Instance Attributes:
        - _item_options:
            The actions which can be carried out on any given item

    Representation Invariants:
        - name != ''
        - description != ''
        - isinstance(start_position, int) and start_position > 0
        - isinstance(target_position, int) and target_position > 0
        - target_points >=
    """

    def __init__(self, name: str, start: int, target: int, target_points: int) -> None:
        """Initialize a new item.
        """

        # NOTES:
        # This is just a suggested starter class for Item.
        # You may change these parameters and the data available for each Item object as you see fit.
        # (The current parameters correspond to the example in the handout).
        # Consider every method in this Item class as a "suggested method".
        #
        # The only thing you must NOT change is the name of this class: Item.
        # All item objects in your game MUST be represented as an instance of this class.

        self.name = name
        self.start_position = start
        self.target_position = target
        self.target_points = target_points


class Player:
    """
    A Player in the text advanture game.


    Instance Attributes:
        - x
            This is the current position of the player in relatiton to the x-axis
        - y
            This is the current position of the player in relatiton to the y-axis
        - inventory
            The items that the player is currently carrying around
        - victory
            Keeps track of if the player has won the game yet
        - moves
            Number of moves the player has left


    Representation Invariants:
        - isinstance(x, int) and x > 0
        - isinstance(y, int) and y > 0
        - isinstance(inventory, list)
        - isinstance(victory, bool)
        - isinstance(game_lost, bool)
        - isinstance(moves, int)
    """

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a new Player at position (x, y).
        """

        # NOTES:
        # I removed the x & y from the initializer to just spawn at (0, 0).
        # This is a suggested starter class for Player.
        # You may change these parameters and the data available for the Player object as you see fit.

        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False
        self.moves = 25

    def move(self, direction: str) -> None:
        """
        This method moves the player in the specified direction.

        """
        direction = direction.lower()
        if direction == 'north':
            self.y += 1
        elif direction == 'south' and self.y > 0:
            self.y -= 1
        elif direction == 'east':
            self.x += 1
        elif direction == 'west' and self.x > 0:
            self.x -= 1

        # self.moves -= 1
        #
        # if self.moves == 0:
        #     self.game_lost = True

    def reverse_move(self, direction: str) -> None:
        """
        This method moves the player in the specified direction.

        """
        direction = direction.lower()
        if direction == 'north' and self.y > 0:
            self.y -= 1
        elif direction == 'south':
            self.y += 1
        elif direction == 'east' and self.x > 0:
            self.x -= 1
        elif direction == 'west':
            self.x += 1

    def add_item(self, item: str) -> None:
        """
        Adds an item to the player's inventory.
        """
        self.inventory.append(item)

    def display_inventory(self) -> None:
        """
        Displays the items in the player's inventory.
        """
        if self.inventory:
            print("Inventory:")
            for item in self.inventory:
                print("-", item)
        else:
            print("Your inventory is empty.")


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map:
            A nested list representation of this world's map.
        - locations:
            A location class storing location information for the world.
        - items:
            A list containing items class objects for the world.

    Representation Invariants:
        - self.map != []
        - self.map[0] != []
    """

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO) -> None:
        """
        Initialize a new World for a text adventure game, based on the data in the given open files.

        - location_data: name of text file containing location data (format left up to you)
        - items_data: name of text file containing item data (format left up to you)
        """

        # NOTES:

        # map_data should refer to an open text file containing map data in a grid format, with integers separated by a
        # space, representing each location, as described in the project handout. Each integer represents a different
        # location, and -1 represents an invalid, inaccessible space.

        # You may ADD parameters/attributes/methods to this class as you see fit.
        # BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES IN THIS CLASS

        # The map MUST be stored in a nested list as described in the load_map() function's docstring below
        self.map = self.load_map(map_data)
        self.locations = self.load_locations(location_data)
        self.items = self.load_items(items_data)

        # NOTE: You may choose how to store location and item data; create your own World methods to handle these
        # accordingly. The only requirements:
        # 1. Make sure the Location class is used to represent each location.
        # 2. Make sure the Item class is used to represent each item.

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def load_map(self, map_data: TextIO) -> list[list[int]]:
        """
        Store map from open file map_data as the map attribute of this object, as a nested list of integers like so:

        If map_data is a file containing the following text:
            1 2 5
            3 -1 4
        then load_map should assign this World object's map to be [[1, 2, 5], [3, -1, 4]].

        Return this list representation of the map.
        """
        lines = map_data.readlines()

        map_lines = []

        for line in lines:
            line = line.strip()
            map_line = []
            for num_str in line.split():
                num_int = int(num_str)  # Convert each substring to an integer
                map_line.append(num_int)
            map_lines.append(map_line)

        return map_lines

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)

         Preconditions:
         - x >= 0
         - y >= 0
        """
        loc = Location("", "", "", "", 0, [], 0, 0, 0)
        if 0 <= x < len(self.map) and 0 <= y < len(self.map[0]):
            location_number = self.map[y][x]
            for location in self.locations:
                if location.location_number == location_number:
                    loc = location

        return loc

    def load_locations(self, location_data: TextIO) -> list[Location]:
        """
        Creates a list of Location objects found in the game world.

        """
        locations = []
        lines = location_data.readlines()

        i = 0
        while i < len(lines):
            name = None
            number = None
            short_description = ""
            long_description = ""
            examined_description = ""
            points = 0

            for line in lines[i:i + 30]:
                line = line.strip()
                if line.startswith("#"):
                    # Skip comments in the file
                    continue

                elif line.startswith("LOCATION"):
                    name = line
                    number = int(line.split()[1])

                # elif line.startswith("0"):
                #     points = int(line)

                elif line and line[0].isdigit():
                    points = int(line)

                elif line.startswith("START1"):
                    short_description = ""
                    i += 1

                    while not lines[i].strip().startswith("END1"):
                        short_description += lines[i].strip() + "\n"
                        i += 1

                elif line.startswith("START2"):

                    long_description = ""
                    i += 1

                    while not lines[i].strip().startswith("END2"):
                        long_description += lines[i].strip() + "\n"
                        i += 1

                elif line.startswith("START3"):

                    examined_description = ""
                    i += 1

                    while not lines[i].strip().startswith("END3"):
                        examined_description += lines[i].strip() + "\n"
                        i += 1

            coordinates = self.get_location_coordinates(number)
            x, y = coordinates

            current_location = Location(name, long_description, short_description, examined_description, number,
                                        [], points, x, y)
            locations.append(current_location)
            i += 30

        return locations

    def load_items(self, items_data) -> list[Item]:
        """
        Loads the game items form the items file onto the game world map.
        """
        items = []
        lines = items_data.readlines()

        # Parse lines and create Item objects
        for line in lines:
            # Parse each line to extract item attributes
            start, target, target_points, name = line.strip().split(',')
            start = int(start)
            target = int(target)
            target_points = int(target_points)
            item = Item(name, start, target, target_points)
            items.append(item)

        return items

    def get_location_coordinates(self, location_number: int) -> Optional[Tuple[int, int]]:
        """
        Returns the coordinates of a location based on its location number.
        If the location number is not found, returns None.
        """
        for y, row in enumerate(self.map):
            for x, num in enumerate(row):
                if num == location_number:
                    return (x, y)
        return None
