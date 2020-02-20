from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':
    
    Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    
    'foyer':
    
    Room(
        "Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    
    'overlook':
    
    Room(
        "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
    
    'narrow':
    
    Room(
        "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
    
    'treasure':
    
    Room(
        
        "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# creating items

item = {

  'fire': Item("Fire Sword", "Destroys anything in one swing"),

  'amulet': Item("Amulet", "Heals you to full health"),

  'boober': Item("Boober", "Makes your boobs huge.")
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Put items in rooms

room['outside'].items = [
  item['fire'],
  item['amulet']
]

room['narrow'].items = [
  item['boober']
]

#
# Main
#

# user = int(input("[1] Rock  [2] Paper   [3] Scissors    [9] Quit\n"))

# Make a new player object that is currently in the 'outside' room.

Anth = Player("Anth", room["outside"])
def printInstructions():
    print('**************************')
    print('* Please input direction to go or action to take')
    print('* Allowed directions are: \n'
            + '*  n to move north\n'
            + '*  s to move south\n'
            + '*  w to move west\n'
            + '*  e to move east')
    print('* Allowed actions are \n* `get item` or `take item` to pick an item\n'
            + '* `drop item` to put an item from your inventory into a room\n' 
            + '* i or inventory to show items in your inventory\n'
            + '* l or list to show items in current room\n'
            + '* where `item` is the name of the item you want to pick or drop')
    print('**************************')


# Write a loop that:
#
# * Prints the current room name
printInstructions()
print(Anth.getCurrentRoom())

# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.
#

while True:
  userChoice = input('\nInput direction to go or action to do: \n')
  splitUserChoice = userChoice.split(' ')
  if len(splitUserChoice) == 2:
    if splitUserChoice[0] == 'take' or splitUserChoice[0] == 'get':

      itemExists = False
      for i in Anth.getCurrentRoom().items:
        if splitUserChoice[1].lower() == i.name.lower():
          itemExists = True

      if itemExists:
        Anth.items.appened(item[splitUserChoice[0].lower()])

        item[splitUserChoice[0].lower()].onTake()

        Anth.getCurrentRoom().items.remove(item[splitUserChoice[1].lower()])
      
      else: 
        print(splitUserChoice[1].capitalize() + ' is not in this room!')

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
