from room import Room
from character import Enemy, Friend
from rpg_info import RPGInfo
from item import Item

dark_house = RPGInfo("the Dark House")
dark_house.welcome()
RPGInfo.info()
RPGInfo.author = "Lyle Wong"

kitchen = Room("Kitchen")
kitchen.set_description("A filthy kitchen that hasn't been cleaned in decades")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with chairs scattered across the floor")

ballroom = Room("Ballroom")
ballroom.set_description("A room with a shiny oak-wood floor.")

print("There are " + str(Room.number_of_rooms) + " rooms to explore.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

lyle = Enemy("Lyle", "A suspicious individual")
lyle.set_conversation("... what are you doing here...")
lyle.set_weakness("knife")
dining_hall.set_character(lyle)

ava = Friend("Ava", "A maid that seems friendly at first glance")
ava.set_conversation("Ooh - hello there, I'm Ava.")
ballroom.set_character(ava)

knife = Item("knife")
knife.set_description("A kitchen tool with a seemingly sharp edge")
kitchen.set_item(knife)

bread = Item("bread")
bread.set_description("Bread completely covered in mould")
dining_hall.set_item(bread)

current_room = kitchen
backpack = []

dead = False
while dead == False:
    print("\n")         
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")
    
    # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
       
    elif command == "fight":
        # You can check whether an object is an instance of a particular
        # class with isinstance() - useful! This code means
        # "If the character is an Enemy"
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if fight_with in backpack:
                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Lucky... you won..")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have defeated all the enemies")
                        dead = True
                else:
                    # What happens if you lose?
                    print("HAHAHAHAHAH YOU LOST THE FIGHT")
                    print("GAME OVER")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("Take a look around... There is noone in this room")        

    elif command == "kiss":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("uhhh... thats a bad idea, just saying....")
            else:
                inhabitant.kiss()
        else:
            print("There is no one here to kiss :(")

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)

RPGInfo.credits()
