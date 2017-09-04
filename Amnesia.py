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
    "up":"in a stairwell.",
    "south":"in a hotel lobby."
    },
    "in a hotel lobby.":{
    "roomDesc":"The front lobby of the hotel is pretty much as drab as the\n" \
    "rooms, dimly lit so that the peeling wallpaper and worn carpets\n" \
    "do not seem so noticeable. A large, curved desk serves as the main\n" \
    "reception counter. The whole place smells like it needs a good airing.\n" \
    "Exits: north, south",
    "north":"at the bottom of a stairwell.",
    "south":"at Kensington High St, outside hotel."
    },
    "at Kensington High St, outside hotel.":{
    "roomDesc":"You are on Kensington High St, a busy shopping thoroughfare in west\n" \
    "London. A small grey building stands before you, a backlit signboard above\n" \
    "the doors spells out 'Holly Day Inn' in large green letters. The pavement\n" \
    "is wide and cleanly swept. Occasionally a busy shopper rushes past, nearly\n" \
    "bumping into you in their haste to be somewhere else.\n" \
    "Exits: north, east, west",
    "north":"in a hotel lobby.",
    "east":"at Kensington High St, outside newsagent.",
    "west":"at Kensington High St, western end."
    },
    "at Kensington High St, outside newsagent.":{
    "roomDesc":"You are on Kensington High St, a busy shopping thoroughfare in west\n" \
    "London. A boarded-up newsagent lies to the south, a sad relic of the\n" \
    "past when people still bought their newspapers and magazines over\n" \
    "counter. Most of these vending jobs have been taken over by robots.\n" \
    "Exits: east, west, north",
    "west":"at Kensington High St, outside hotel.",
    "north":"on Church St, southern end.",
    "east":"at the corner of Ken High St and Victoria Rd."
    },
    "on Church St, southern end.":{
    "roomDesc":"This is the southern, trendy end of Church St which becomes edgier\n" \
    "the further north you go. There is a beautiful old church at the corner,\n" \
    "surrounded by a few dilapidated stone tombs. A leafy plane tree\n" \
    "offers a scrap of shade over the pavement.\n"
    "Exits: south, north",
    "south":"at Kensington High St, outside newsagent."
    },
    "at Kensington High St, western end.":{
    "roomDesc":"This is the western end of Kensington High St where the shops\n" \
    "tail off and the residential buildings begin. To the north lies\n" \
    "the genteel Holland Park, a peaceful retreat from the bustling high\n" \
    "street. The wrought iron gates are open. The road continues west \n" \
    "towards the borough of Hammersmith.\n" \
    "Exits: east, west, north",
    "east":"at Kensington High St, outside hotel.",
    "north":"in Holland Park.",
    "west":"on Hammersmith Rd."
    },
    "in Holland Park.":{
    "roomDesc":"The park is serene and well-kept. The lawn is regularly tended\n" \
    "to by robot gardeners that keep the grass pristine and free\n" \
    "of weeds. All the hedges and trees have been manicured to perfection,\n" \
    "not a single leaf is out of place. There is a wooden bench here\n" \
    "where tired strollers can rest awhile.\n" \
    "Exits: north, south",
    "south":"at Kensington High St, western end.",
    "north":"deep in Holland Park."
    },
    "deep in Holland Park.":{
    "roomDesc":"This part of the park has been partly neglected by the robot gardeners,\n" \
    "perhaps due to a bug in the program, a small triangle of grass has been\n" \
    "left unmown and it is home to many butterflies in the summer, attracted\n" \
    "by the abundance of wildflowers. The grass is almost knee-high and you\n" \
    "entertain a passing fancy that perhaps you could find your GPS if you\n" \
    "searched it.\n" \
    "Exits: south",
    "south":"in Holland Park."
    },
    "at the corner of Ken High St and Victoria Rd.":{
    "roomDesc":"You are at the junction of Kensington High Street and Victoria Road\n" \
    "which runs south, lined with many shops and stately mansions. Traffic gets\n" \
    "quite busy around here.\n" \
    "Exits: west, south",
    "west":"at Kensington High St, outside newsagent.",
    "south":"at the northern end of Victoria Rd."
    },
    "at the northern end of Victoria Rd.":{
    "roomDesc":"The northern end of Victoria Rd is rather posh and leafy, running\n" \
    "through a mostly residential neighbourhood but there is one cafe here, the\n" \
    "Florentine Cafe which has been operating for years. It has a few tables out\n" \
    "on the pavement, covered with gingham tablecloths. Most patrons prefer to\n" \
    "sit indoors though, as it is well into autumn now.\n" \
    "Exits: north, east",
    "north":"at the corner of Ken High St and Victoria Rd.",
    "east":"in the Florentine Cafe."
    },
    "in the Florentine Cafe.":{
    "roomDesc":"The cafe interior is actually quite small with space only for a\n" \
    "handful of tables and chairs. The leather chairs are actually quite comfy\n" \
    "and inviting. But everything has the worn patina of age, the furnishings are\n" \
    "a little shabby and dreary. It gradually strikes you that you are the only\n" \
    "customer in this cafe.\n" \
    "Exits: west",
    "west":"at the northern end of Victoria Rd."
    },
    "on Hammersmith Rd.":{
    "roomDesc":"Hammersmith Road runs west towards the borough of Hammersmith. The\n" \
    "shops around here are mostly generic but one pub stands out to the north,\n" \
    "the Rabid Cow. It has a hand-painted sign of a black cow frothing at the\n" \
    "mouth hanging above the doorway. It looks like a fairly traditional English\n" \
    "pub, with windowboxes full of fading pansies.\n" \
    "Exits: east, north",
    "east":"at Kensington High St, western end."
    }
}

items = {
    "inside a Hotel Room.": ("towel","phone"),
    "in the hotel corridor.":(),
    "in a stairwell.":(),
    "at the bottom of a stairwell.":(),
    "in a hotel lobby.":(),
    "at Kensington High St, outside hotel.":(),
    "at Kensington High St, outside newsagent.":(),
    "on Church St, southern end.":(),
    "at Kensington High St, western end.":(),
    "in Holland Park.":(),
    "deep in Holland Park.":(),
    "at the corner of Ken High St and Victoria Rd.":(),
    "at the northern end of Victoria Rd.":(),
    "in the Florentine Cafe.":(),
    "on Hammersmith Rd.":()
}

itemDescs = {
    "towel":"This threadbare towel is monogrammed with the initials of the\n" \
            "hotel. It has a slightly moldy odour.",
    "phone":"A small mobile phone. You can probably use it to make calls.",
    "newspaper":"The newspaper has the current date printed on the top- 21 Oct 2092.\n" \
    "The headlines are all about the new leader of the world, Goggle's\n" \
    "president and CEO, trialling a new internet search engine that can\n" \
    "predict your searches even before the thoughts form in your head.\n" \
    "Another is about a blazing war between automatons on a distant \n" \
    "continent. All of it makes you feel vaguely depressed, apart from\n" \
    "the Daily Crossword on page 3. But you realise your head still throbs\n" \
    "too much to contemplate doing a crossworld puzzle so you give up and\n" \
    "close the newspaper.",
    "ball":"This chewy rubber ball is probably a dog's lost toy. You could\n" \
    "throw it, if you had a dog."
}

NPCs = {
    "in a hotel lobby.":"Hotel Manager",
    "at Kensington High St, outside newsagent.":"Robot Newsagent",
    "on Church St, southern end.":"Old Beggar",
    "in the Florentine Cafe.":"Waitress"
}

NPCdescs = {
    "hotel manager":"The Hotel Manager gazes at you with heavy-lidded eyes, dozy from\n" \
    "having had little sleep. His oily hair is slicked back in an\n" \
    "effort to appear neat and punctilious but it just gives him the\n" \
    "air of a two-bit gangster. He looks somewhat uncomfortable in an\n" \
    "ill-fitting cheap suit.",
    "robot newsagent":"The shiny Robot Newsagent looks like a midget with a glass dome\n" \
    "for a head. It bears a tiny screen that says:\n" \
    "<press 1> for The Propaganda Times\n" \
    "<press 2> for the Daily Hell\n" \
    "There are two flashing buttons on the robot's chest.",
    "old beggar":"The Old Beggar is dressed in stringy rags, with plastic\n"
    "bags for shoes. For some reason, he is completely drenched, probably\n" \
    "from a recent downpour. His pathetic clothes are dripping wet and he\n" \
    "is quivering from the autumn chill. His sad, brown eyes regard you\n" \
    "with a mixture of hope and suspicion.",
    "biggs":"Biggs is a burly chap with a sanguine disposition. He spends his\n" \
    "days down at the local bar, having a few drinks and laughs with whoever\n" \
    "will listen to him rambling about his old geocaching exploits. Of\n" \
    "uncertain occupation, you will often find him wandering the parks,\n" \
    "feeding the pigeons with scraps, when he's not propping up the bar\n" \
    "at The Rabid Cow.",
    "waitress":"The young waitress looks interminably bored, as she has been standing\n" \
    "at the counter all morning without a single customer to serve. She can't wait\n" \
    "for the day she passes her job on to an automaton, for then she'd be free to\n" \
    "indulge her real passion, which is doing crossword puzzles. She is a puzzle\n" \
    "fiend, much like the rest of the population!"
   }

NPCchats = {
    "in a hotel lobby.":("The Hotel Manager clears his throat and chuckles: \n" \
                         "'You were in pretty rough shape when you were dragged in last night.'\n",
                     "'That fella Biggs saved your skin. You were completely wasted!'\n",
                     "'If you ever find him again, tell him he forgot to pay your bill.'\n",
                     "'Doesn't matter because you happened to have the EXACT amount in your purse!'\n",
                     "The Hotel Manager leans back with an evil glint in his eye, sniggering at you.\n",
                     "'Oh! Don't forget, check-out time is 2PM. Have a nice day!'\n"),
    "on Church St, southern end.":("The Old Beggar eyes you up and down, his dull eyes flicker with recognition.\n",
                                   "'You are a... geocacher? If you aren't, you surely look like one!'\n",
                                   "'You won't find me rooting around in them bushes! Ha ha!'\n",
                                   "The Old Beggar lets out a hoarse laugh and then coughs violently into his sleeve.\n",
                                   "'I used to drive a taxi, until these bloody self-driving vehicles took over\n" \
                                   "our roads! Totally ruined me, it did. There's no honest work left for\n" \
                                   "people like me.'\n",
                                   "'I ain't got a friend in the world left. Maybe just old Biggs....'\n",
                                   "'He spends his days idling, living off his missus. Lucky sod!'\n",
                                   "The Old Beggar coughs again and sniffles. Sounds like a bad case of croup."
                                   ),
    "in Holland Park.":("Biggs smiles kindly at you as you greet him uncertainly.",
                        "'Hello, my friend! Feeling better? You had a little too much to drink last night.'\n",
                        "Biggs chortles to himself and continues:\n" \
                        "'You fell down and banged your head pretty hard. You feeling OK?'\n",
                        "Biggs frowns. 'Do you remember anything at all from last night?'\n",
                        "'You were telling me you had solved this D5 puzzle. A really HARD one\n" \
                        "that no one has yet found. You had the coordinates in your GPS and you\n" \
                        "were heading off to find the cache.'\n",
                        "Biggs scratches his chin thoughtfully. \n" \
                        "'I guess someone who works for Big Sue heard you and got TOO interested...'\n",
                        "'Don't you know? Big Sue has found EVERY single geocache ever published in\n" \
                        "the country, except this one! She's desperate to get her hands on the\n" \
                        "coordinates!'",
                        "Biggs starts to giggle like a child.\n" \
                        "'Must have slipped something in your drink. You had a really CRAZY time\n" \
                        "until you fell. Guess those stilletoes were a BAD idea.'\n",
                        "Biggs barely stifles another giggle at the memory. \n" \
                        "'Big Sue's heavies rifled through your pockets, must have got\n" \
                        "your GPS. Don't look at me. I gave up geocaching years ago.\n" \
                        "Must admit, I got a tad stroppy when they archived a cache of\n" \
                        "mine without any warning.'\n",
                        "Biggs allows himself a brief, bitter smirk, and then all is well again.",
                        "'I took you to a nearby hotel to let you sleep it off.'\n",
                        "'Don't thank me! I'd do it for anyone!'\n"
                        ),
    "in the Florentine Cafe.":("The Waitress sighs and regards you impatiently.\n" \
                              "'Are you going to order anything or are you just going to stand there?'\n",
                              "'Most people just prefer their insta-nutri drinks nowadays! No one\n" \
                              "even comes in for a croissant or toast anymore.'\n",
                              "The Waitress grumbles: 'It's so boring! I'd rather be doing something fun.'\n",
                              "The Waitress prods you: 'Do you even have money for a coffee?'\n",
                              "'You have to pay, we're not a charity, you know!'\n"
                              )
}

tasksCompleted = {
    "at Kensington High St, outside newsagent.":False,
    "on Church St, southern end.":False,
    "deep in Holland Park.":False
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


def moveItemToRoom(roomLocation,itemStr):
    itemsInRoom = list(items[roomLocation])
    itemsInRoom.append(itemStr)
    items[roomLocation] = itemsInRoom

showTitle()

while True:
    
    move = ""
    while move == "":
        move = raw_input("> ")

    move = move.lower().split()

    if move[0] == "look" and len(move) < 2:
        #return room description
        print rooms[currentRoom]["roomDesc"]
        
        if currentRoom in items:
            #There are items in the room
            if len(items[currentRoom])>0:
                itemlist = ", ".join(items[currentRoom])
                print "You see: " + itemlist
        
        if currentRoom in NPCs:
            #There are NPCs in the room
            print NPCs[currentRoom] + " is here."

    if move[0] == "look" and len(move) > 2:
        npcStr = move[2:]
        npcSearchStr = " ".join(npcStr)
        if npcSearchStr in NPCdescs:
            print NPCdescs[npcSearchStr]
        else:
            print "You don't see that here!"

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

    if move[0] == "talk":
        if currentRoom in NPCchats:
            dialogue = NPCchats[currentRoom]
            for chat in dialogue:
                print chat
                raw_input("Press any key to continue...")
        else:
            print "There is no one here to talk to."

    if move[0] == "press":
        if not tasksCompleted[currentRoom]:
            if move[1] in ("1","2"):
                print "You push a button on the robot and it clicks and whirrs momentarily."
                print "It emits a high pitched whining noise as it prints out the newspaper."
                print "Clunk! It spits out a freshly-printed newspaper from the flap situated\n" \
                "roughly around the robot's crotch.\n" \
                "The newspaper drops unceremoniously to the ground."
                moveItemToRoom(currentRoom,"newspaper")
                tasksCompleted[currentRoom] = True
            else:
                print "You need to press 1 or 2. Try again!"
        else:
            print "You push the button repeatedly but the Robot remains idle.\nSo much for modern technology!"

    if move[0] == "give" and len(move) > 2:
        itemToGive = move[1]
        target = " ".join(move[3:])
        if itemToGive not in inventory:
            print "You cannot give what you haven't got!"
        elif currentRoom not in NPCs:
            print "There is no one here to give it to."
        elif target not in ("old beggar","waitress"):
            print "This is not the right place nor time for giving!" 
        else:
            inventory.remove(itemToGive)
            print "You give the " + itemToGive + " to the " + target + "."
            #check place where this occurs
            if target == "old beggar" and itemToGive == "towel" and not tasksCompleted[currentRoom]:
                tasksCompleted[currentRoom] = True
                print "The Old Beggar gasps in gratitude. He grabs the towel and begins to dry\n" \
                "himself. It does the job adequately and the beggar looks relieved."
                print "He says: 'You can find old Biggs in the park. Please say hello for me.'\n"
                #move Biggs to park bench
                NPCs["in Holland Park."]="Biggs"
            if target== "waitress" and itemToGive == "newspaper":
                print "The Waitress brightens up! She opens the newspaper to page 3 and proceeds\n" \
                "to finish the Daily Crossword at lightning pace. Then, she frowns,\n" \
                "turning to ask you if you knew a 10-letter word starting with M and ending\n" \
                "with A-D-E that meant a disguise, or a masked costume party? That'll be\n" \
                "the answer to 12 Down..."

                
    if move[0] == "search" and len(move) > 1:
        if not tasksCompleted[currentRoom]:
            if move[1] == "grass":
                print "You search the tall grass and uncover an old rubber ball."
                moveItemToRoom(currentRoom,"ball")
                tasksCompleted[currentRoom] = True
            else:
                print "Search what?"
        else:
            print "It is pointless to spend so much time searching the grass!"

