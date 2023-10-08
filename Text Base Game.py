class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = {}
        self.exits = {}

    def add_item(self, item):
        self.items[item.name] = item

    def remove_item(self, item):
        if item.name in self.items:
            del self.items[item.name]

    def add_exit(self, direction, room):
        self.exits[direction] = room

class Player:
    def __init__(self):
        self.inventory = []

    def take_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

def display_inventory(player):
    if player.inventory:
        print("Inventory:")
        for item in player.inventory:
            print(f"- {item.name}")
    else:
        print("Your inventory is empty.")

def main():
    # Create items
    key = Item("Key", "A rusty old key")
    sword = Item("Sword", "A sharp sword")
    potion = Item("Potion", "A healing potion")

    # Create rooms
    start_room = Room("Start Room", "You are in a dimly lit room.")
    hallway = Room("Hallway", "You are in a long hallway.")
    treasure_room = Room("Treasure Room", "You have found the treasure room!")

    # Add items to rooms
    start_room.add_item(key)
    hallway.add_item(sword)
    treasure_room.add_item(potion)

    # Define room exits
    start_room.add_exit("east", hallway)
    hallway.add_exit("west", start_room)
    hallway.add_exit("east", treasure_room)
    treasure_room.add_exit("west", hallway)

    # Initialize player
    player = Player()

    current_room = start_room

    print("Text-based Adventure Game")
    print("=========================")
    print(current_room.description)

    while True:
        command = input("What do you want to do? ").strip().lower()

        if command == "quit":
            print("Thank you for playing!")
            break
        elif command == "look around":
            print(current_room.description)
            display_inventory(player)
        elif "take " in command:
            item_name = command[5:]
            if item_name in current_room.items:
                item = current_room.items[item_name]
                player.take_item(item)
                current_room.remove_item(item)
                print(f"You have taken the {item.name}.")
            else:
                print(f"There is no {item_name} here.")
        elif "drop " in command:
            item_name = command[5:]
            if item_name in [item.name for item in player.inventory]:
                item = next(item for item in player.inventory if item.name == item_name)
                player.drop_item(item)
                current_room.add_item(item)
                print(f"You have dropped the {item.name}.")
            else:
                print(f"You don't have a {item_name}.")
        elif command in current_room.exits:
            current_room = current_room.exits[command]
            print(current_room.description)
        else:
            print("Invalid command. Try 'look around', 'take [item]', 'drop [item]', or 'quit'.")

if __name__ == "__main__":
    main()