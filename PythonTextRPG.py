import sys
import os
import time

screen_width = 100


# player setup ##

class Player:
    def __init__(self):
        self.name = ""
        self.job = ""
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False


myPlayer = Player()


# title screen ##

def title_screen_selections():
    option = input("> ")
    if option.lower() == "play":
        setup_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()
    elif option.lower() == "back":
        title_screen()
    while option.lower() not in ['play', 'help', 'quit', 'back']:
        print("please enter a valid command")
        option = input("> ")
        if option.lower() == "play":
            setup_game()
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            sys.exit()


def title_screen():
    os.system('clear')
    print('######################################')
    print('###### Welcome To The Text RPG! ######')
    print('######################################')
    print('                --Play--              ')
    print('                --Help--              ')
    print('                --Back--              ')
    print('                --Quit--              ')
    print("  Don't worry i Don't Copy Write 2021 ")
    print("######################################")
    title_screen_selections()


# Help Screen ##

def help_menu():
    print('##################################################')
    print('############ Welcome To The Text RPG! ############')
    print('##################################################')
    print('# Move:"W, A, S, D"  Or  "Up, Down, Left, Right" #')
    print('#         -- Type Commands To Do Them --         #')
    print("#      -- Use: 'look' To Inspect Thing's --      #")
    print("#         !!!!!   Enjoy The Ride   !!!!!         #")
    print("##################################################")
    print("##################################################")
    title_screen_selections()


# Game Functionality ##

def start_game():
    # map
    """

    a1a2a3a4 # Player starts at b2
    ~~~~~~~~~
    | | | | |a4
    ~~~~~~~~~
    | |x| | |b4
    ~~~~~~~~~
    | | | | |c4
    ~~~~~~~~~
    | | | | |d4
    ~~~~~~~~~
    d1d2d3d4
    """


# ZONE VALUES
ZONENAME = ''
DESCRIPTION = "description"
EXAMINATION = "examine"
SOLVED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False
                 }
zonemap = {
    'a1': {
        ZONENAME: 'Hospital',
        DESCRIPTION: "Mandela's Royal Hospital",
        EXAMINATION: "looks like it was built some time between 01:42Am and 01:43Am",
        SOLVED: False,
        UP: "",
        DOWN: "b1",
        LEFT: "",
        RIGHT: "a2",
    },
    'a2': {
        ZONENAME: 'Barbers Shop',
        DESCRIPTION: "ol Man Benny's Barber Shop",
        EXAMINATION: "the sign reads:- open= weekdays  12 - 4, weekends 9 till the sun rises woah, please visit me",
        SOLVED: False,
        UP: "",
        DOWN: "b2",
        LEFT: "a1",
        RIGHT: "a3",
    },
    'a3': {
        ZONENAME: 'Town Hall',
        DESCRIPTION: "A Grand And Beautiful Repurposed Cathedral",
        EXAMINATION: "you enjoy the pictures of the funnily dressed people in the stain glass window",
        SOLVED: False,
        UP: "",
        DOWN: "b3",
        LEFT: "a2",
        RIGHT: "a4",
    },
    'a4': {
        ZONENAME: 'Alfrids Bunny House',
        DESCRIPTION: "you can here loud music and saw people going"
                     " in and out every 3 minutes but it just looks like a badly ran night club",
        EXAMINATION: "you are curious to go inside, but you "
                     "remember your dad coming home after a night out here, your mother kicked him out",
        SOLVED: False,
        UP: "",
        DOWN: "b4",
        LEFT: "a3",
        RIGHT: "",
    },
    'b1': {
        ZONENAME: 'A Well',
        DESCRIPTION: "a cobble stone water well with a spindle crank but no handle, rope and bucket. ",
        EXAMINATION: "their is a glisten from the surface of the"
                     " water but its a long way down, if only you had a windless",
        SOLVED: False,
        UP: "a1",
        DOWN: "c1",
        LEFT: "",
        RIGHT: "b2",
    },
    'b2': {
        ZONENAME: 'Home',
        DESCRIPTION: "This is where you live!",
        EXAMINATION: "It's just a tad warm, but your home looks the same. ",
        SOLVED: False,
        UP: "a2",
        DOWN: "c2",
        LEFT: "b1",
        RIGHT: "b3",
    },
    'b3': {
        ZONENAME: 'Pond De La Sploosh',
        DESCRIPTION: "dogs come here for adventure and butt sniffs,"
                     " some times you wonder what the meaning of life is, but than you hear the borks and feel giddy",
        EXAMINATION: "the pond looks pondyer than ever, the tention"
                     " in your leg relaxes as the damn creeps through your clothes",
        SOLVED: False,
        UP: "a3",
        DOWN: "c3",
        LEFT: "b2",
        RIGHT: "b4",
    },
    'b4': {
        ZONENAME: 'Wet Space Manor House',
        DESCRIPTION: "this plot of land actually holds the ashes of"
                     " catapillar who spontaneously combusted when"
                     " i were about 6, seems fitting to spread them somewhere called wet",
        EXAMINATION: "you look into the window and an old lady "
                     "wearing only a leaf is looking back at you, "
                     "the competition begins and neither of you "
                     "blink for the entirety of all stars by "
                     "smash mouth, you look down and notice "
                     "finally that her boobs are made of rock "
                     "and she is infact a sculptor of marble, "
                     "a little ashamed you walk away only to remember you didn't lose the stare off",
        SOLVED: False,
        UP: "a4",
        DOWN: "c4",
        LEFT: "b3",
        RIGHT: "",
    },
    'c1': {
        ZONENAME: 'Post Office',
        DESCRIPTION: "the post office is where you come to send your mail through the post",
        EXAMINATION: "going in you can see a well dressed and very "
                     "approachable young lady, you try to remember her name but poof, you get embarrassed and leave",
        SOLVED: False,
        UP: "b1",
        DOWN: "d1",
        LEFT: "",
        RIGHT: "c2",
    },
    'c2': {
        ZONENAME: 'Town Square',
        DESCRIPTION: "a small market place and seating area in one "
                     "corner in the middle their seems to be people"
                     " talking to each other, you wonder if anyone you know is around here",
        EXAMINATION: "you see Jemma walking with her parrot on her"
                     " shoulder , you smile at each other in passing and carry on about your day",
        SOLVED: False,
        UP: "b2",
        DOWN: "d2",
        LEFT: "c1",
        RIGHT: "c3",
    },
    'c3': {
        ZONENAME: 'Train Station',
        DESCRIPTION: "steam locomotives like to come here a lot for some reason",
        EXAMINATION: "the people flooding in and out of the front "
                     "door seem either panicked or relaxed as they "
                     "scour for their trains you notice a young you"
                     " are starting to feel like your in they're way so you leave",
        SOLVED: False,
        UP: "b3",
        DOWN: "d3",
        LEFT: "c2",
        RIGHT: "c4",
    },
    'c4': {
        ZONENAME: 'Wonder Walk Dogge Park',
        DESCRIPTION: "dogs come here for adventure and butt sniffs,"
                     " some times you wonder what the meaning of life is, but than you hear the borks and feel giddy",
        EXAMINATION: "13 dogs are running in perfect parallel after"
                     " one very lucky postman, but wait theres a"
                     " twist, or more a flip, he does a flip into"
                     " the wet space manor house garden and is bright red, you smile and carry on about your day",
        SOLVED: False,
        UP: "b4",
        DOWN: "d4",
        LEFT: "c3",
        RIGHT: "",
    },
    'd1': {
        ZONENAME: 'Cafe Poe Sippers',
        DESCRIPTION: "the only good coffee shop for 50 miles , you' d know you did your research",
        EXAMINATION: "you smell toasted coffee and steaming hot "
                     "cakes, cookies, brownies and *sniffs-deeply*"
                     " ... dog poo , you look down and realise you trod in poop",
        SOLVED: False,
        UP: "c1",
        DOWN: "",
        LEFT: "",
        RIGHT: "d2",
    },
    'd2': {
        ZONENAME: 'Bojangles Cottage',
        DESCRIPTION: "cute as can be, jus like miss bojangles",
        EXAMINATION: "it looks so tiny on the outside but you can"
                     " tell its bigger inside from the mystical portal mirror next to the telly",
        SOLVED: False,
        UP: "c2",
        DOWN: "",
        LEFT: "d1",
        RIGHT: "d3",
    },
    'd3': {
        ZONENAME: 'Traps Speak Easy',
        DESCRIPTION: "Traps the place to be when its hot outside, if you get my drift",
        EXAMINATION: "you love this place but ordering food is a"
                     " pain because the waiters where sound"
                     " proofing headphones, you always wander why they do that , but it is busy every time you go",
        SOLVED: False,
        UP: "c3",
        DOWN: "",
        LEFT: "d2",
        RIGHT: "d4",
    },
    'd4': {
        ZONENAME: 'Wonder Walk Dogge Park',
        DESCRIPTION: "dogs come here for adventure and butt sniffs"
                     ", some times you wonder what the meaning of life is, but than you hear the borks and feel giddy",
        EXAMINATION: "you look at the grass and intend to wooof"
                     " however a good boi pokes your booty and"
                     " you contemplate chasing him, he grabs the "
                     "stick you were stood on and darts for the nearest hooman",
        SOLVED: False,
        UP: "c4",
        DOWN: "",
        LEFT: "d3",
        RIGHT: "",
    }
}


#  GAME INTERACTIVITY ##
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))


def prompt():
    print("\n" + "====================================")
    print("what would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'look']
    while action.lower() not in acceptable_actions:
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'look']:
        player_examine(action.lower())


def player_move(action):
    ask = "where would you like to move to?\n"
    dest = input(ask)
    if dest in ["up", "north"]:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ["down", "south"]:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest in ["left", "west"]:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ["right", "east"]:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)


def movement_handler(destination):
    print("\n" + "you have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()


def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("you have done every thing there is to do here")
    else:
        print("you feel like your missing something here")


# GAME FUNCTIONALITY ####

def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
    # here handle if puzzles have been solved , spoke to everyone and completed there puzzles
    # boss defeated
    # became a hero
    # got the girl
    # ect , ect


def setup_game():
    os.system('clear')

    # NAME collection ##

    question1 = "Hello, whats your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    player_name = input("> ")
    myPlayer.name = player_name

    # JOB collection ##

    question2 = "An whats your job?\n"
    question2added = "(you can be a mage, priest or a warrior)\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ")
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("ok, you are now a " + player_job + "!\n")
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("ok, you are now a " + player_job + "!\n")
    myPlayer.job = player_job

    # PLAYER STATS ###

    if myPlayer is 'warrior':
        myPlayer.hp = [120]
        myPlayer.mp = [40]
    if myPlayer.job == 'mage':
        myPlayer.hp = [40]
        myPlayer.mp = [120]
    if myPlayer.job == 'priest':
        myPlayer.hp = [80]
        myPlayer.mp = [80]

    # INTRODUCTION ###
    question3 = "Welcome" + player_name + "the" + player_job + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)

    speech1 = "Welcome to Verstustan"
    speech2 = "im so glad to finally see you " + player_name + \
              ", the creator told me such great things are too come of you."
    speech3 = "remember to hehe not get sucked in"
    speech4 = "after all its just ... a .. game ..."
    speech5 = ".... hehe ...haha ... Haha ....HaHA..hehEhahahHAHAHAHAHAH"

    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.09)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.15)
    for character in speech5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)

    os.system('clear')
    print('###################################################')
    print('##############   And So It Began    ###############')
    print('###################################################')
    main_game_loop()


title_screen()

# the tutorial you forgot about dom haha
# byron tong
# https://www.youtube.com/watch?v=ERLT1iU0DVY&list=PL1-slM0ZOosX2HXlRPzSNMTXGeWW7gbLi&index=7
