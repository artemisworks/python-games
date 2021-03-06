#!/usr/bin/python

#AMNESIA - v1.0
#Copyright 2017 JR ONG (artemisworks)

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
    "past when people still bought their newspapers and magazines over the\n" \
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
    "offers passers-by a scrap of shade over the pavement.\n"
    "Exits: south, north",
    "south":"at Kensington High St, outside newsagent.",
    "north":"on Church St, northern end."
    },
    "on Church St, northern end.":{
    "roomDesc":"The road narrows a bit further north towards Notting Hill Gate.\n" \
    "The shops around here specialise in 21st century antique electronics.\n" \
    "If you hunt around, you might even find an early Garmin 250 unit in\n" \
    "mint condition. A tall red-brick building with an entrance porch lies\n" \
    "east. It is mostly unexpectional except you notice all its curtains\n" \
    "are tightly drawn.\n" \
    "Exits: south, east",
    "south":"on Church St, southern end.",
    "east":"in front of red-brick flats."
    },
    "in front of red-brick flats.":{
    "roomDesc":"You stand before an anonymous red-brick building and the front door bears\n" \
    "the number '33' in small bronze letters. There are a few buzzers mounted\n" \
    "beside the door, one for each flat in the building.\n" \
    "Exits: west",
    "west":"on Church St, northern end."
    },
    "on a first floor landing.":{
    "roomDesc":"This is the first floor landing of a block of flats. A carpeted\n" \
    "staircase leads up and down from here. There is a door here painted in dull,\n" \
    "camouflage colours and you can hear loud music throbbing through the paper-\n" \
    "thin walls.\n" \
    "Exits: east, down",
    "down":"in front of red-brick flats.",
    "east":"in Big Sue's living room."
    },
    "in Big Sue's living room.":{
    "roomDesc":"Big Sue's living room is rather untidy, a jumble of furniture, plush\n" \
    "cushions and interesting geocache containers of all shapes and sizes.\n" \
    "There is even a huge pile of parallel sticks arranged in a corner as a\n" \
    "conversation piece. You instinctively feel tempted to search it. Some\n"
    "awful early 2000's music is being pumped through the wi-fi speakers.\n" \
    "A few people are here already, all dressed up in masks and costumes.\n" \
    "Someone here is wearing a yellow radiation suit. You can't really tell if\n" \
    "Big Sue is around.\n" \
    "Exits: west", 
    "west":"on a first floor landing."
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
    "perhaps due to a bug in their algorithm, a small triangle of grass has been\n" \
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
    "handful of tables and chairs. The saggy leather chairs are actually quite\n" \
    "nice to sink into. But everything has the worn patina of age, the furnishings are\n" \
    "a little shabby and dreary. It gradually strikes you that you are the only\n" \
    "customer in this cafe.\n" \
    "Exits: west",
    "west":"at the northern end of Victoria Rd."
    },
    "on Victoria Rd, outside mansion.":{
    "roomDesc":"About halfway down Victoria Road, you spy a sprawling mansion whose grand\n" \
    "facade has been almost obscured by wisteria. Enormous willow trees crowd\n" \
    "the front garden, affording the occupants maximum privacy. The property is\n" \
    "surrounded by a moderately high brick wall. A brass plaque by the front gate\n" \
    "reads simply: 'CRYPTIC'.\n"
    "Exits: north",
    "north":"at the northern end of Victoria Rd."
    },
    "in front garden of mansion.":{
    "roomDesc":"The front garden of the grand mansion is somewhat overgrown with\n" \
    "unkempt bushes and towering willow trees that flank the gravel driveway\n" \
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
    "is really the impressive mahogany desk by the window. It has been\n" \
    "polished so perfectly that it gleams like a mirror. A slim laptop\n" \
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
    "roomDesc":"The pub interior is cosy and dark, with a small fire glowing in\n" \
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
    "on Church St, northern end.":[],
    "in front of red-brick flats.":[],
    "on a first floor landing.":[],
    "in Big Sue's living room.":[],
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
    "scrap":"This is a torn scrap of yellow note paper on which someone has\n" \
    "scrawled the numbers: 83... The rest of it has been ripped off. Perhaps\n" \
    "it is even in your own handwriting but you don't remember.",
    "ball":"This chewy rubber ball is probably a dog's lost toy. You could\n" \
    "throw it, if you had a dog.",
    "flyer":"This is an advertisement for a local pizza delivery company.\n" \
    "Just call 818 for BEST-PIZZA!",
    "laptop":"This slim computer laptop is really lightweight, with a sleek\n" \
    "black screen and tiny but functional keyboard. You will need\n" \
    "to activate it to turn the screen on. There is a post-it note\n" \
    "stuck on the lid with a pencilled scrawl: 'answer to 12 down'",
    "ticket":"This is a ticket to Big Sue's fancy dress party. The address is\n" \
    "33 Church Street. Dress code: FANCY is MANDATORY.",
    "mask":"This is a blue Did Not Find sad-face mask with eyeholes. It is\n" \
    "designed to completely obscure the face of the wearer.",
    "ammobox":"This ammo box is the Porsche of all geocache containers. Sadly quite\n" \
    "rare these days, this particular box dates back to 2001. It rattles as you\n" \
    "shake it as there is something inside. You might be able to open it.",
    "gps":"This is your trusty GPS unit, back in your hands at last. You can\n" \
    "get it to 'navigate' to your final destination so you can claim the\n" \
    "geocache and sign the logbook. You hope you can remember your name...",
    "note":"This is a torn note. On it, someone has scrawled the numbers ..58\n" \
    "but the first half is missing. This must be part of the code\n" \
    "that Big Sue was looking for!"
}

NPCs = {
    "in a hotel lobby.":"Hotel Manager",
    "at Kensington High St, outside newsagent.":"Robot Newsagent",
    "on Church St, southern end.":"Old Beggar",
    "in the Florentine Cafe.":"Waitress",
    "inside The Rabid Cow pub.":"Bartender",
    "in front garden of mansion.":"German Shepherd",
    "in the Party shop.":"Kylie",
    "in front of red-brick flats.":"Bouncer",
    "in Big Sue's living room.":"Signal"
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
    "enormous fangs at you as you approach, snapping and growling. You\n" \
    "sense it can easily take you down if you make a wrong move!",
    "bartender":"The Bartender is a jolly sort, accustomed to seeing all kinds of\n" \
    "people drift through his pub, from illustrious nobility to the\n" \
    "dregs of humanity. It is not clear what end of the scale he sees\n" \
    "you at, but his blue eyes twinkle when he catches you looking at him.\n" \
    "Clearly, he has seen you before and witnessed your stellar performance\n" \
    "before you fell unconscious and lost your memory!",
    "kylie":"Kylie was named after her great-grandmother and you can tell she's\n" \
    "annoyed at being called some name that is soooo last century!\n" \
    "She is a bubbly, vicacious teenager who simply loves her job here at\n" \
    "the Party Shop when she's not preoccupied with her boyfriend Jason.",
    "bouncer":"This hulk of a guy probably eats people like you for breakfast. He\n" \
    "is at least seven-foot tall and built like an Abrams tank. Suited up\n" \
    "in Armani and reeking of expensive cologne, he also sports a humongous ruby\n" \
    "ring with which he likes carving his initials into his victims' cheeks.\n" \
    "Mess with him at your own peril!",
    "signal":"Someone here is dressed up as Signal the Frog. It lumbers about\n" \
    "a bit awkwardly in the unwieldy costume, gripping a glass of punch. It\n" \
    "sees you and raises its glass in greeting. Cheers and happy geocaching!"
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
                                   "'You won't find me rooting around in them bushes!'\n",
                                   "The Old Beggar sighs deeply and then coughs violently into his sleeve.\n",
                                   "'I used to drive a taxi, until these bloody self-driving vehicles took over\n" \
                                   "our roads! Totally ruined me, it did. There's no honest work left for\n" \
                                   "people like me.'\n",
                                   "'I ain't got a friend in the world left. Maybe just old Biggs....'\n",
                                   "'He spends his days idling, living off his missus. Lucky sod!'\n",
                                   "The Old Beggar coughs violently again. Sounds like a bad case of croup."
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
                        "coordinates!'\n",
                        "Biggs tries tactfully to stifle a grin.\n" \
                        "'Must have slipped something in your drink. You had a really CRAZY time\n" \
                        "until you fell. Guess those stilletoes were a BAD idea.'\n",
                        "Biggs continues with apparent relish at relating the story. \n" \
                        "'Big Sue's heavies rifled through your pockets, they must have got\n" \
                        "your GPS. There was a bit of a scuffle.'\n",
                        "'I did however, manage to save this for you. I don't know what it means\n" \
                        "but it might be important. It fell from your pocket while you were being\n" \
                        "roughed up by those chaps.'\n",
                        "Biggs hands you a torn scrap of paper.\n",
                        "'I used to hunt geocaches myself, a long time ago. I know how you feel.\n" \
                        "Must admit, I got a tad stroppy when they archived a cache of\n" \
                        "mine without any warning.'\n",
                        "Biggs allows himself a brief, bitter smirk, and then all is well again.\n",
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
                        "'Lady Cryptic who sets the puzzles in all our newspapers is rolling\n" \
                        "in dough. Big Sue wants to turn geocaching into a commercial enterprise,'\n" \
                        "huge and popular enough to rival even crossword puzzles!'\n",
                        "'The Mother of all Enterprises! YUGE! She told me so herself.'\n",
                        "With that, the Bartender pats his sizeable paunch and guffaws again.\n" \
                        "'She told me she just needs to crack some secret code or other, and\n" \
                        "then she'll find that LAST puzzle cache. Anyway, she expects to\n" \
                        "do this SOON. She's even throwing a party to celebrate. After all,\n" \
                        "she thinks she's almost got it all sewn up!'\n",
                        "The Bartender pauses in his monologue and peers at you again.\n" \
                        "'Tell you what, you need an aspirin, that's what it is.'\n",
                        "As he laughs again, your head aches even more at the thought that Big Sue\n" \
                        "might actually get the geocache before you! You need to get your GPS back...\n" \
                        "and pronto!\n"  
                                 ),
    "in the Party shop.":("Kylie smiles brightly and cheerfully: 'Welcome to the Party Shop!'\n",
                        "'Feel free to browse but remember I'm here to help!'\n",
                        "Kylie paces around the room, rubbing her stomach.\n",
                        "'I can't wait for my lunch break. I'm so HUNGRY, I could eat a horse.'\n",
                        "'But my boss says I have to stay here until 3PM! Arrghh!'\n",
                        "Kylie rolls her eyes and pouts:\n" \
                        "'I'll simply DIE if I have to wait until 3PM for lunch!'\n"
                        ),
    "in front of red-brick flats.":(
        "The Bouncer folds his thick arms across his chest and growls.\n" \
        "'What's your business here? Are you a party guest?'\n",
        "A truly chilling look creeps into the bouncer's stony grey eyes.\n" \
        "'If you're here for Big Sue's party, give me your ticket! Or an invitation?'\n",
        "'If you're just here for the view, lemme give you some advice. CLEAR OFF!'\n"
        ),
    "in Big Sue's living room.":(
        "Signal cocks its head to one side and wiggles its bum cheekily.\n",
        "It has a chirpy female voice. 'Hi there, welcome to my party!'\n",
        "'Grab yourself a drink and mingle! Everyone's a geocacher here.'\n",
        "'But of course, I'm the BEST. Soon I will have found every blinking cache\n" \
        "in the country! Reason to celebrate, don't you think?'\n",
        "Signal starts to bop to the beaty music. You feel your headache coming back.\n"
        )
}

tasksCompleted = {
    "at Kensington High St, outside newsagent.":False,
    "on Church St, southern end.":False,
    "FirstScrapGiven":False,
    "deep in Holland Park.":False,
    "on Victoria Rd, outside mansion.":False,
    "ThrowBall":False,
    "in back garden of mansion.":False,
    "in a mansion library.":False,
    "WearMask":False,
    "SearchSticks":False,
    "OpenAmmobox":False,
    "SecondScrapGiven":False,
    "CompleteCode":False
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
        drop <item> - drop an object in your inventory
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

    elif move[0] == "look" and len(move) > 2:
        npcStr = move[2:]
        npcSearchStr = " ".join(npcStr)
        if npcSearchStr in NPCdescs:
            print NPCdescs[npcSearchStr]
        else:
            print "You don't see that here!"

    elif move[0] == "status":
        showStatus()

    elif move[0] == "quit":
        #quit game and exit
        print "You return to your boring reality... Goodbye!\n"
        break

    elif move[0] == "help":
        showHelp()

    elif move[0] == "get":
        if move[1] in items[currentRoom]:
            #if the item is present in the room
            print "You get a " + move[1] + "."
            inventory.append(move[1])
            itemsInRoom = list(items[currentRoom])
            itemsInRoom.remove(move[1])
            items[currentRoom] = itemsInRoom
            
        else:
            print "That is not here."

    elif move[0] == "drop" and len(move) > 1:
        #check if item is in inventory
        itemToDrop = move[1]
        if itemToDrop in inventory:
            print "You drop the " + itemToDrop + "."
            inventory.remove(itemToDrop)
            items[currentRoom].append(itemToDrop)
            #special case of mask, set to un-worn!
            if itemToDrop == "mask":
                tasksCompleted["WearMask"] = False
        else:
            print "You don't have the item on you."

    elif move[0] == "examine" and len(move) > 1:
        #check if item to examine is in inventory
        itemToExamine = move[1]
        if itemToExamine in inventory:
            print itemDescs[itemToExamine]
        else:
            print "It must be in your possession before you can examine it."
    elif move[0] == "examine" and len(move) < 2:
        print "Examine what?"

    elif move[0] in ("north","south","east","west","down","up"):
        #we are moving in a direction
        moveDir = move[0]
        if moveDir in rooms[currentRoom]:
            #if this is a valid direction
            currentRoom = rooms[currentRoom][moveDir]
            print "You go " + moveDir + "."
            showStatus()
        else:
            print "You cannot go that way!"

    elif move[0] == "talk":
        if currentRoom in NPCchats:
            dialogue = NPCchats[currentRoom]
            print "You try to strike up a conversation."
            for chat in dialogue:
                raw_input("....continue....")
                print chat
            if currentRoom == "in Holland Park.":
                if not tasksCompleted["FirstScrapGiven"]:
                    inventory.append("scrap")
                    tasksCompleted["FirstScrapGiven"] = True

                    #check if complete code has been obtained
                    if tasksCompleted["SecondScrapGiven"]:
                        tasksCompleted["CompleteCode"]=True
        else:
            print "There is no one here to talk to."

    elif move[0] == "press":
        if currentRoom == "at Kensington High St, outside newsagent.":
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
        else:
            print "There is nothing here to press."            

    elif move[0] == "give" and len(move) > 2:
        itemToGive = move[1]
        target = " ".join(move[3:])
        if itemToGive not in inventory:
            print "You cannot give what you haven't got!"
        elif currentRoom not in NPCs:
            print "There is no one here to give it to."
        elif target not in ("old beggar","waitress","bouncer"):
            print "You don't really want to do that!" 
        else:
            #check place where this occurs
            if target == "old beggar" and itemToGive == "towel" and currentRoom == "on Church St, southern end.":
                inventory.remove(itemToGive)
                print "You give the " + itemToGive + " to the " + target + "."
                print "The Old Beggar gasps in gratitude. He grabs the towel and begins to dry\n" \
                "himself. It does the job adequately and the beggar looks relieved."
                print "He says: 'You can find old Biggs in the park. Please say hello for me.'\n"
                #move Biggs to park bench
                NPCs["in Holland Park."]="Biggs"
            elif target== "waitress" and itemToGive == "newspaper" and currentRoom == "in the Florentine Cafe.":
                inventory.remove(itemToGive)
                print "You give the " + itemToGive + " to the " + target + "."
                print "The Waitress brightens up! She opens the newspaper to page 3 and proceeds\n" \
                "to finish the Daily Crossword at lightning pace. Then, she frowns,\n" \
                "turning to ask you if you knew a 10-letter word starting with M and ending\n" \
                "with A-D-E that meant a disguise, or a masked costume party? That'll be\n" \
                "the answer to 12 Down..."
            elif target=="bouncer" and itemToGive == "ticket" and currentRoom == "in front of red-brick flats.":
                inventory.remove(itemToGive)
                print "You give the " + itemToGive + " to the " + target + "."
                print "The Bouncer looks surprised that you had a ticket after all."
                print "He duly steps aside, opens the front door and waves you in."
                print "'Straight down the hallway and up the stairs to the first floor!'"
                raw_input("...continue...")
                print "You enter the hallway and quickly ascend the staircase."
                currentRoom = "on a first floor landing."
            else:
                print "This is not the right place nor time for giving!"
                
    elif move[0] == "search" and len(move) > 1:
        if currentRoom == "deep in Holland Park.":
            if not tasksCompleted[currentRoom]:
                if move[1] == "grass":
                    print "You search the tall grass and uncover an old rubber ball."
                    moveItemToRoom(currentRoom,"ball")
                    tasksCompleted[currentRoom] = True
                else:
                    print "What do you wish to search?"
            else:
                print "It is pointless to spend so much time searching around."
        elif currentRoom == "in Big Sue's living room.":
            if move[1] in ("sticks","parallel"):
                if tasksCompleted["WearMask"] and not tasksCompleted["SearchSticks"]:
                    print "You search the parallel sticks and uncover an ammo box underneath!"
                    print "Luckily for you, the other party guests seem too preoccupied to notice.\n"
                    moveItemToRoom(currentRoom,"ammobox")
                    tasksCompleted["SearchSticks"] = True
                elif tasksCompleted["WearMask"] and tasksCompleted["SearchSticks"]:
                    print "Don't waste your time searching interminably!"
                else:
                    #the end for the player
                    print "As you begin your search, suddenly you feel a furry hand on your shoulder."
                    print "It's Signal the Frog. It has removed its mask. It's actually Big Sue\n" \
                    "herself! One of her henchmen must have recognised your face and alerted her\n" \
                    "to your presence at her party. You're done for!\n"
                    raw_input("...continue...")
                    print "You struggle but her grip is just too tight, like a steel vise!"
                    print "One of the party guests opens a window... it's a drop of at least\n" \
                    "twenty, thirty feet...."
                    raw_input("...continue...")
                    print "You are carried to the window, shouting incoherently. The last words\n" \
                    "you hear are Big Sue saying...'The geocache is MINE, all MINE....'"
                    print "They let go of you and you fall.... everything fades to black...."
                    print "\t\tTHE END.\n\n"
                    print "(perhaps you'd like to try again?)"
                    break
            else:
                print "What do you want to search?"

    elif move[0] == "climb" and len(move) > 1:
        if move[1] == "wall" and currentRoom == "on Victoria Rd, outside mansion.":
            if not tasksCompleted["ThrowBall"]:
                print "You heave yourself over the wall and land heavily on your feet,\n" \
                "almost twisting your ankle. Almost immediately, you can hear loud and\n" \
                "ferocious barking!"
                currentRoom = "in front garden of mansion."
            else:
                print "You heave yourself over the wall and land heavily on your feet,\n" \
                "almost twisting your ankle. You find yourself in a somewhat overgrown\n" \
                "front garden. There is a gap in the hedge you can enter."
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

    elif move[0] == "throw" and len(move) > 1:
        if move[1] == "ball":
            if "ball" in inventory:
                if currentRoom == "in front garden of mansion.":
                    print "You hurl the ball as hard as you can into a thicket of bramble about\n" \
                    "forty feet away. The dog stops barking momentarily, and then runs after it!\n" 
                    print "You are safe, but not for long! You spy a small gap in the hedge nearby,\n" \
                    "which you could possibly enter."
                    inventory.remove("ball")
                    tasksCompleted["ThrowBall"] = True
                    del NPCs["in front garden of mansion."]
                else:
                    print "You hurl the ball as hard as you can, and watch it arc into the distance.\n"
                    inventory.remove("ball")
            else:
                print "You don't even have a ball to throw."
        else:
            print "You cannot throw that, it would be highly inappropriate."

    elif move[0] == "enter" and len(move) > 1:
        if move[1] in ("gap","hedge") and currentRoom == "in front garden of mansion.":
            if "in front garden of mansion." in NPCs: 
                print "You can't move anywhere or the dog might maul you to death!"
            else:
                print "You push yourself through the small gap in the hedge. It is a\n" \
                "tight squeeze but you make it through to the back garden.\n"
                currentRoom = "in back garden of mansion."
        
        elif move[1] == "window" and currentRoom == "in back garden of mansion.":
            if tasksCompleted[currentRoom]:
                print "Ignoring the jagged, broken shards of glass, you climb into the\n" \
                "mansion through the open window, feeling like a crack burglar.\n"
                currentRoom = "in a mansion library."
            else:
                print "The window is locked shut, you cannot enter it, unless...."
        else:
            print "Enter what exactly?"

    elif move[0] == "break" and len(move) > 1:
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

    elif move[0] == "activate":
        if "laptop" in inventory:
            print "You press a key to activate the laptop and the black screen flickers to life."
            pwd = raw_input("Enter password:")
            if pwd.strip().lower() == "masquerade":
                if not tasksCompleted["in a mansion library."]:
                    print "Login successful! Downloading email...1 NEW Message\n"
                    print "Sender: bigsue@MistressOfGeocaching.com"
                    print "Subject: Fancy dress party - celebration!"
                    print "...Sending attachment to wi-fi printer... *Whirrr, clack*\n"
                    tasksCompleted["in a mansion library."] = True
                    moveItemToRoom("in a mansion library.","ticket")
                else:
                    print "Login successful. No new e-mails."
            else:
                print "Login failed.\n"
                print "The screen suddenly goes black again."
        else:
            print "What exactly do you want to activate?"

    elif move[0] == "dial":
        if "phone" in inventory:
            print "You would be better off typing: call <number>"
        else:
            print "You will need a phone to do that."

    elif move[0] == "call" and len(move)>1:
        if "phone" in inventory:
            if currentRoom == "in the Party shop.":
                if move[1] == "818":
                    print "You call BEST-PIZZA and order a takeaway pizza with all the toppings and\n" \
                    "extra cheese and pepperoni."
                    raw_input("...continue...")
                    print "Kylie jumps for joy! She is so pleased that she decides to show you the\n" \
                    "latest item in stock, and wants you to have it for free since you were so kind\n" \
                    "to order her a pizza! It is in fact, a DNF mask!"
                    moveItemToRoom(currentRoom,"mask")
                    raw_input("...continue...")
                    print "The phone disintegrates in your pocket, having exhausted its useful life.\n" \
                    "This is built-in obsolescence in action."
                    inventory.remove("phone")
                else:
                    print "You call " + move[1] + " but there is no answer."
            else:
                print "There is a right time and place to make that phone call."
        else:
            print "But you don't have a phone!"
    
    elif move[0] == "wear" and len(move) > 1:
        if move[1] == "mask":
            if "mask" in inventory:
                if not tasksCompleted["WearMask"]:
                    tasksCompleted["WearMask"] = True
                    print "You wear the mask. It is certainly an improvement!"
                else:
                    print "You are already wearing the mask."
            else:
                print "You do not have a mask to wear!"
        else:
            print "You can't wear that, stop mucking around!"

    elif move[0] == "smash":
      print "Try another word for that?"
      
    elif move[0] == "open" and len(move) > 1:
        if move[1] in ("ammobox","box","ammo box"):
            if "ammobox" in inventory and not tasksCompleted["OpenAmmobox"]:
                print "You prise open the ammo box and your trusty GPS is lying inside!"
                print "This is where Big Sue was hiding it all along! You pick up the GPS."
                print "There is also a torn note which you retrieve.\n"
                inventory.append("gps")
                inventory.append("note")
                tasksCompleted["OpenAmmobox"] = True
                tasksCompleted["SecondScrapGiven"] = True

                if tasksCompleted["FirstScrapGiven"] and tasksCompleted["SecondScrapGiven"]:
                    tasksCompleted["CompleteCode"] = True

            elif tasksCompleted["OpenAmmobox"]:
                print "The ammo box is already open."
            elif "ammobox" not in inventory:
                print "You don't have the ammo box!"
        else:
            print "You can't open that, sorry."

    elif move[0] == "read":
        print "You can try to 'examine' the item instead."

    elif move[0] == "navigate":
        if "gps" in inventory:
            if tasksCompleted["CompleteCode"]:
                #WIN GAME
                print "You press the navigate button on the GPS."
                print "The screen readout says: \n" \
                "<< Navigating to N51 29.988  W000 10.806 >>\n"
                raw_input("...continue...")
                print "You scurry out onto the streets as fast as your legs will carry you\n" \
                "and find yourself walking down Kensington High St once again.\n"
                raw_input("...continue...")
                print "The last of your headache ebbs away and as you increase your pace along\n" \
                "the pavement, the memories come flooding back!\n"
                raw_input("...continue...")
                print "Your pulse quickens. The road arrives at a junction here, there is a\n" \
                "mighty statue of a man on a horse. There are embassies around you so you\n" \
                "are forced to be discreet.\n"
                raw_input("...continue...")
                print "Walking further down the road, you remind yourself not to search the\n" \
                "railings of any private buildings here. Not the railings! Don't arouse\n" \
                "suspicion or get yourself arrested!\n"
                raw_input("...continue...")
                print "You stop at a suitable spot for parking and chaining up a bike,\n" \
                "close to a shady tree. Looking downwards, you recognise a familiar\n" \
                "logo... you realise with immense relief that you have regained\n" \
                "your memory AND found the elusive geocache!\n"
                raw_input("...continue...")
                print "All that remains is to work out how to use the secret code...but that\n" \
                "is no problem for a crack geocacher like you.\n"
                raw_input("...continue...")
                print "Now go and write your name in the logbook. For real. This is\n"
                print """
    T H E  E N D !
   
     _  _
    (_)_(_)
     (o o)
    ==\o/==

Please report any bugs or mice to Artemisworks using
the usual contact methods.

"""
                break
            else:
                print "You press the navigate button on your GPS..."
                print "However, you realise that you still need that secret code to\n" \
                "find the cache. There's still some more work to be done!"
        else:
            print "How do you expect to navigate without a GPS?"



    else:
        print "What?"
