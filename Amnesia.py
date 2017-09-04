#!/usr/bin/python

inventory = []

currentRoom = "inside a Hotel Room."

rooms = {
    "inside a Hotel Room.": {
        "roomDesc":"This is a non-descript hotel room, as anonymous as any drab\n" \
        "budget motel in the city. There is a faint hum of a central\n" \
        "heating unit and somewhere nearby, a leaky tap is softly dripping.\n" \
        "A grey and tousled double bed dominates the cramped space.\n" \
        "Exits: north\n",
    "north":"in the hotel corridor."
    },
    "in the hotel corridor.": {
        "roomDesc":"The narrow corridor stretches past a few more doors\n" \
        "and leads into a dimly-lit fire escape stairwell.\n" \
        "Exits: north, south\n",
    "south":"inside a Hotel Room.",
    "north":"in a stairwell."
    },
    "in a stairwell.":{
        "roomDesc":"The staircase only leads down. The lighting here is so dim\n" \
        "that you can barely see where to walk.\n" \
        "Exits: south, down",
    "south":"in the hotel corridor.",
    "down":"at the bottom of a stairwell."
    },
    "at the bottom of a stairwell.":{
        "roomDesc":"You are at the bottom of a fire escape staircase. The lights\n" \
        "are so dim you have to strain your eyes to see anything. A closed\n" \
        "fire door leads south. A brass sign on it reads 'RECEPTION'.\n" \
        "Exits: south, up",
    "up":"in a stairwell."

    }
}

items = {
    "inside a Hotel Room.": ("towel","phone"),
    "in the hotel corridor.":(),
    "in a stairwell.":(),
    "at the bottom of a stairwell.":()
}

itemDescs = {
    "towel":"This threadbare towel is monogrammed with the initials of the\n" \
            "hotel. It has a slightly moldy odour.",
    "phone":"A small mobile phone. You can probably use it to make calls."
}

def showTitle():
    print """
  ___                            _       
 / _ \                          (_)      
/ /_\ \_ __ ___  _ __   ___  ___ _  __ _ 
|  _  | '_ ` _ \| '_ \ / _ \/ __| |/ _` |
| | | | | | | | | | | |  __/\__ \ | (_| |
\_| |_/_| |_| |_|_| |_|\___||___/_|\__,_|
                                         
                                         

\tA text adventure game by Artemisworks

"""

    raw_input("Press any key to continue...")
    print "You wake up with a throbbing headache, your mouth furred\n" \
    "from last night's drinking. Peeling open your eyes, you find \n" \
    "yourself in an unfamiliar environment, lying alone in a strange\n" \
    "bed. You are still fully dressed in your usual geocaching outfit\n" \
    "but your purse, money and GPS are gone. Even worse, you can\n" \
    "vaguely remember that you were on an important mission but can\n" \
    "no longer recall what it is."
    print "Type 'help' for basic instructions."

def showStatus():
    #show player's current status and inventory
    print "You are " + currentRoom
    print "Inventory: " + ", ".join(inventory)


showTitle()

while True:
    
    move = ""
    while move == "":
        move = raw_input("> ")

    move = move.lower().split()

    if move[0] == "look":
        #return room description
        print rooms[currentRoom]["roomDesc"]
        
        if currentRoom in items:
            if len(items[currentRoom])>0:
                itemlist = ", ".join(items[currentRoom])
                print "You see: " + itemlist

    if move[0] == "status":
        showStatus()
    if move[0] == "quit":
        #quit game and exit
        print "You return to your boring reality... Goodbye!\n"
        break
    if move[0] == "get":
        if move[1] in items[currentRoom]:
            #if the item is present in the room
            print "You get a " + move[1] + "."
            inventory.append(move[1])
            itemsInRoom = list(items[currentRoom])
            itemsInRoom.remove(move[1])
            items[currentRoom] = itemsInRoom
            #Remove the room altogether if all items are gone
            #if len(itemsInRoom)== 0:
            #    del items[currentRoom]
        else:
            print "That is not here."

    if move[0] == "examine" and len(move) > 1:
        #check if item to examine is in inventory
        itemToExamine = move[1]
        if itemToExamine in inventory:
            print itemDescs[itemToExamine]
        else:
            print "It must be in your possession before you can examine it."
    elif move[0] == "examine" and len(move) < 2:
        print "Examine what?"

    if move[0] in ("north","south","east","west","down","up"):
        #we are moving in a direction
        moveDir = move[0]
        if moveDir in rooms[currentRoom]:
            #if this is a valid direction
            currentRoom = rooms[currentRoom][moveDir]
            print "You go " + moveDir + "."
            showStatus()
        else:
            print "You cannot go that way!"
