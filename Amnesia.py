#!/usr/bin/python

inventory = []

currentRoom = "inside a hotel room."

rooms = {
    "inside a hotel room.": {
        "roomDesc":"This is a non-descript hotel room, as anonymous as any drab\n" \
        "budget motel in the city. There is a faint hum of a central\n" \
        "heating unit and somewhere nearby, a leaky tap is softly dripping.\n" \
        "A grey and tousled double bed dominates the cramped space.\n" \
        "Exits: north",
    "north":"in the hotel corridor."
    },
    "in the hotel corridor.": {
        "roomDesc":"The narrow corridor stretches past a few more doors\n" \
        "and leads into a dimly-lit fire escape stairwell.\n" \
        "Exits: north, south\n",
    "south":"inside a hotel room.",
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
    "Exits: north, south, east",
    "north":"at the corner of Ken High St and Victoria Rd.",
    "east":"in the Florentine Cafe.",
    "south":"on Victoria Rd, outside mansion."
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
    "on Victoria Rd, outside mansion.":{
    "roomDesc":"About halfway down Victoria Road, you spy a sprawling mansion whose grand\n" \
    "facade has been almost obscured by a huge wisteria. Enormous willow trees\n" \
    "crowd the front garden, affording the occupants maximum privacy. This is\n" \
    "surrounded by a moderately high brick wall. A brass plaque by the front gate\n" \
    "reads simply: 'CRYPTIC'.\n"
    "Exits: north",
    "north":"at the northern end of Victoria Rd."
    },
    "in front garden of mansion.":{
    "roomDesc":"The front garden of the grand mansion is somewhat overgrown with\n" \
    "unkempt bushes and towering willow trees that flank the gravel driveway leading\n" \
    "leading to the house. The main gate to the road lies to your west, which\n" \
    "you can open easily from the inside.\n" \
    "Exits: west",
    "west":"on Victoria Rd, outside mansion."
    },
    "in back garden of mansion.":{
    "roomDesc":"The back garden of the mansion is a pretty planted lawn whose\n" \
    "centrepiece is a fine marble bust of Lady Cryptic herself. The bust\n" \
    "is surrounded by a small patchwork of flowers, resembling a crossword.\n" \
    "There is a large window here through which you can glimpse a capacious,\n" \
    "well-stocked library.\n" \
    "Exits: west",
    "west":"in front garden of mansion."
    },
    "in a mansion library.":{
    "roomDesc":"The shelves of this immense room are lined with leather-bound books\n" \
    "with arcane titles in gold lettering. But what draws your attention\n" \
    "is really the impressive mahogany desk by the window. A slim laptop\n" \
    "and a printer are the only items on the desk. Jagged slivers of glass\n" \
    "are scattered like tiny jewels all over the plush carpet.\n" \
    "Exits: south",
    "south":"in back garden of mansion."
    },
    "on Hammersmith Rd.":{
    "roomDesc":"Hammersmith Road runs west towards the borough of Hammersmith. The\n" \
    "shops around here are mostly generic but one pub stands out to the north,\n" \
    "the Rabid Cow. It has a hand-painted sign of a black cow frothing at the\n" \
    "mouth hanging above the doorway. It looks like a fairly traditional English\n" \
    "pub, its pretty windowboxes replete with fading pansies.\n" \
    "Exits: east, west, north",
    "east":"at Kensington High St, western end.",
    "north":"inside The Rabid Cow pub.",
    "west":"on Hammersmith Rd, western end."
    },
    "inside The Rabid Cow pub.":{
    "roomDesc":"The pub interior is spacious and dark, with a small fire glowing in\n" \
    "the brick fireplace. Empty beer glasses have been left uncollected on\n" \
    "the tables. There are numerous faux leather stools where the locals sit\n" \
    "and drink their woes away and the bar itself is set off to one side. The\n" \
    "air in here is pungent with a familiar, malodorous blend of stale beer\n" \
    "and vomit.\n" \
    "Exits: south",
    "south":"on Hammersmith Rd."
    },
    "on Hammersmith Rd, western end.":{
    "roomDesc":"The road runs east from Hammersmith gyratory towards the trendy\n" \
    "shopping district of Kensington High St. The lugubrious character of the\n" \
    "quiet buildings around here is not helped by the layer of soot and dust\n" \
    "deposited over the years. In startling contrast, a brightly painted shop\n" \
    "lies immediately south, its entrance flanked by a festoon of colourful\n" \
    "balloons. It's the !!!PARTY!!! shop.\n" \
    "Exits: east, south",
    "east":"on Hammersmith Rd.",
    "south":"in the Party shop."
    },
    "in the Party shop.":{
    "roomDesc":"Standing in the Party Shop, you are amazed at the array of costumes\n" \
    "and other party paraphernalia stocked on its overburdened shelves.\n" \
    "You could spend all day here, rooting through the mountains of crepe\n" \
    "party favours, but you have more important things on your mind and no\n" \
    "time to waste.\n" \
    "Exits: north",
    "north":"on Hammersmith Rd, western end."
    }
}

items = {
    "inside a hotel room.": ["towel","phone"],
    "in the hotel corridor.":[],
    "in a stairwell.":[],
    "at the bottom of a stairwell.":[],
    "in a hotel lobby.":[],
    "at Kensington High St, outside hotel.":[],
    "at Kensington High St, outside newsagent.":[],
    "on Church St, southern end.":[],
    "at Kensington High St, western end.":[],
    "in Holland Park.":[],
    "deep in Holland Park.":[],
    "at the corner of Ken High St and Victoria Rd.":[],
    "at the northern end of Victoria Rd.":[],
    "in the Florentine Cafe.":[],
    "on Hammersmith Rd.":[],
    "on Hammersmith Rd, western end.":[],
    "inside The Rabid Cow pub.": ["flyer"],
    "in the Party shop.":[],
    "on Victoria Rd, outside mansion.":[],
    "in front garden of mansion.":[],
    "in back garden of mansion.":[],
    "in a mansion library.":["laptop"]
}

itemDescs = {
    "towel":"This threadbare towel is monogrammed with the initials of the\n" \
            "hotel. It has a slightly moldy odour.",
    "phone":"A small, plastic mobile phone. You can probably use it to\n" \
    "call someone, that is, if you can still remember anyone's number.\n" \
    "It has one credit left.",
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
    "throw it, if you had a dog.",
    "flyer":"This is an advertisement for a local pizza delivery company.\n" \
    "Just call 818 for BEST-PIZZA!",
    "laptop":"This slim computer laptop is really lightweight, with a sleek\n" \
    "black screen and tiny but functional keyboard. You will need\n" \
    "to activate it to turn the screen on. There is a post-it note stuck\n" \
    "on the lid with a pencilled scrawl: 'answer to 12 down'",
    "ticket":"This is a ticket to Big Sue's fancy dress party. The address is\n" \
    "33 Church Street.",
    "mask":"This is a Guy Fawkes mask with eyeholes. You can wear it."
}

NPCs = {
    "in a hotel lobby.":"Hotel Manager",
    "at Kensington High St, outside newsagent.":"Robot Newsagent",
    "on Church St, southern end.":"Old Beggar",
    "in the Florentine Cafe.":"Waitress",
    "inside The Rabid Cow pub.":"Bartender",
    "in front garden of mansion.":"German Shepherd",
    "in the Party shop.":"Kylie"
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
    "fiend, much like the rest of the population.",
    "german shepherd":"This HUGE dog is clearly guarding the mansion. It bares its\n" \
    "enormous fangs at you as you approach, snapping and growling. You sense it\n" \
    "can easily take you down if you make a wrong move!",
    "bartender":"The Bartender is a jolly sort, accustomed to seeing all kinds of\n" \
    "people drift through his pub, from illustrious nobility to the\n" \
    "dregs of humanity. It is not clear what end of the scale he sees\n" \
    "you at, but his blue eyes twinkle when he catches you looking at him.\n" \
    "Clearly, he has seen you before and witnessed your stellar performance\n" \
    "before you fell unconscious and lost your memory!",
    "kylie":"Kylie was named after her great-grandmother and you can tell she's\n" \
    "unhappy at being called some name that was fashionable over a century ago.\n" \
    "She is a bubbly, vicacious teenager who simply loves her job here at\n" \
    "the Party Shop when she's not preoccupied with her boyfriend Jason."
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
                              ),
    "inside The Rabid Cow pub.":("The Bartender polishes the bar with a rag and heaves a big, theatrical sigh.",
                        "'Oh so you're back. Don't think you're getting another drink until you\n" \
                        "get your head sorted out...'\n",
                        "The Bartender throws his head back and laughs uproariously. You fail to see the joke.\n",
                        "'Just remember one thing. Those thugs that messed with you? They work for Big Sue.'\n" \
                        "'Big Sue is the preeminent geocacher of our times!'\n",
                        "'Next to crossword puzzles, geocaching is the biggest 'in' thing right now.'\n",
                        "'That Lady Cryptic who sets the puzzles in all our newspapers is well rolling\n" \
                        "in dough. Big Sue wants to turn geocaching into a commercial enterprise.'\n",
                        "'The Mother of all Enterprises! YUGE! She told me so herself.'\n",
                        "With that, the Bartender rubs his sizeable paunch and laughs again.\n" \
                        "'If she hadn't fallen and broken her leg, she'd have found that last puzzle\n" \
                        "cache by now! Anyway, she expects to find it SOON. She's even throwing a\n" \
                        "huge fancy dress party to celebrate. After all, she thinks she's got it in\n" \
                        "the bag!'\n",
                        "The Bartender pauses in his monologue and peers at you again.\n" \
                        "'Tell you what, you need an aspirin, that's what it is.'\n",
                        "As he laughs again, your head throbs even more at the thought that Big Sue\n" \
                        "might actually get the geocache BEFORE you. You need to get your GPS back...\n" \
                        "and FAST!\n"  
                                 ),
    "in the Party shop.":("Kylie smiles brightly and cheerfully: 'Welcome to the Party Shop!'\n",
                        "'Feel free to browse but remember I'm here to help!'\n",
                        "Kylie paces around the room, rubbing her stomach.\n",
                        "'I can't wait for my lunch break. I'm so HUNGRY, I could eat a horse.'\n",
                        "'But my boss says I have to stay here until 3PM! Arrghh!'\n",
                        "Kylie rolls her eyes and pouts:\n" \
                        "'I'll simply DIE if I have to wait until 3PM for lunch!'\n"
                        )
}

tasksCompleted = {
    "at Kensington High St, outside newsagent.":False,
    "on Church St, southern end.":False,
    "deep in Holland Park.":False,
    "on Victoria Rd, outside mansion.":False,
    "in back garden of mansion.":False,
    "in a mansion library":False
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

def showHelp():
    #show basic instructions
    print """
           Basic Commands:
           ---------------
        look - to check out your environment
        look at <person> - to look over a person in your environment
        talk - to communicate with a person in the room
        get <item> - to pick up an object and move it into your inventory
        examine <item> - to inspect an item you have in your inventory
        give <item> to <person> - to give an item to a person in the room
        status - to show your location and inventory
        north,south,east,west - to move in that direction
        help - to show this menu
        quit - to quit the game 

        Bear in mind there are other commands not listed here that you
        will need to use in the course of the game.

    """

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

    if move[0] == "help":
        showHelp()

    if move[0] == "get":
        if move[1] in items[currentRoom]:
            #if the item is present in the room
            print "You get a " + move[1] + "."
            inventory.append(move[1])
            itemsInRoom = list(items[currentRoom])
            itemsInRoom.remove(move[1])
            items[currentRoom] = itemsInRoom
            
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
            print "It is pointless to spend so much time searching around."

    if move[0] == "climb" and len(move) > 1:
        if move[1] == "wall" and currentRoom == "on Victoria Rd, outside mansion.":
            if not tasksCompleted[currentRoom]:
                print "You heave yourself over the wall and land heavily on your feet,\n" \
                "almost twisting your ankle. Almost immediately, you can hear loud and\n" \
                "ferocious barking!"
                currentRoom = "in front garden of mansion."
            else:
                print "You heave yourself over the wall and land heavily on your feet,\n" \
                "almost twisting your ankle. You find yourself in a somewhat overgrown\n" \
                "front garden."
                currentRoom = "in front garden of mansion."
        elif move[1] == "window" and currentRoom == "in back garden of mansion.":
            if tasksCompleted[currentRoom]:
                print "Ignoring the jagged, broken shards of glass, you climb into the\n" \
                "mansion through the open window, feeling like a crack burglar.\n"
                currentRoom = "in a mansion library."
            else:
                print "The window is locked shut, you cannot climb through it, unless...." 
        else:
            print "What do you wish to climb?"

    if move[0] == "throw" and len(move) > 1:
        if move[1] == "ball":
            if "ball" in inventory:
                if currentRoom == "in front garden of mansion.":
                    print "You hurl the ball as hard as you can into a thicket of bramble about\n" \
                    "forty feet away. The dog stops barking momentarily, and then runs after it!\n" 
                    print "You are safe, but not for long! You spy a small gap in the hedge nearby,\n" \
                    "which you could possibly enter."
                    inventory.remove("ball")
                    del NPCs["in front garden of mansion."]
                else:
                    print "You hurl the ball as hard as you can, and watch it arc into the distance.\n"
                    inventory.remove("ball")
            else:
                print "You don't even have a ball to throw."
        else:
            print "You cannot throw that, it would be highly inappropriate."

    if move[0] == "enter" and len(move) > 1:
        if move[1] in ("gap","hedge") and currentRoom == "in front garden of mansion.":
            if "in front garden of mansion." in NPCs: 
                print "You can't move anywhere or the dog might maul you to death!"
            else:
                print "You push yourself through the small gap in the hedge. It is a\n" \
                "tight squeeze but you make it through to the back garden.\n"
                currentRoom = "in back garden of mansion."
        else:
            print "Enter what exactly?"

    if move[0] == "break" and len(move) > 1:
        if move[1] in ("window","glass") and currentRoom == "in back garden of mansion.":
            if tasksCompleted[currentRoom]:
                print "The window is already broken, you vandal!"
            else:
                tasksCompleted[currentRoom] = True
                print "You heave the small bust of Lady Cryptic into the big glass window!"
                print "There is a satisfyingly LOUD sound of glass smashing into a million\n" \
                "pieces! You shield yourself from the flying shards.\n"
        else:
            print "You'd better not do that here."

    if move[0] == "activate":
        if "laptop" in inventory:
            print "You press a key to activate the laptop and the black screen flickers to life."
            pwd = raw_input("Enter password:")
            if pwd.strip().lower() == "masquerade":
                print "Login successful! Downloading email...1 NEW message\n"
                print "Sender: bigsue@MistressOfGeocaching.com"
                print "Subject: Let's party!!!!!"
                print "Output emails to wi-fi printer. *Whirrr, clack*\n"
                tasksCompleted["in a mansion library."] = True
                moveItemToRoom("in a mansion library.","ticket")
            else:
                print "Login failed.\n"
                print "The screen suddenly goes black again."
        else:
            print "What exactly do you want to activate?"

    if move[0] == "dial":
        if "phone" in inventory:
            print "You would be better off typing: call <number>"
        else:
            print "You will need a phone to do that."

    if move[0] == "call" and len(move)>1:
        if "phone" in inventory:
            if currentRoom == "in the Party shop.":
                if move[1] == "818":
                    print "You call BEST-PIZZA and order a takeaway pizza with all the toppings and\n" \
                    "extra cheese and pepperoni."
                    print "Kylie jumps for joy! She is so pleased that she decides to show you the\n" \
                    "latest item in stock, and wants you to have it for free!\n"
                    moveItemToRoom(currentRoom,"mask")
                    print "The phone disintegrates in your pocket, having exhausted its useful life.\n" \
                    "This is built-in obsolescence in action."
                    inventory.remove("phone")
                else:
                    print "You call " + move[1] + " but there is no answer."
            else:
                print "There is a right time and place to make that phone call."
        else:
            print "But you don't have a phone!"
               

