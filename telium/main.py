#Telium – The game

import random
import sys

from telium.super_secret.super_secret import play_video

#Global variables
num_modules = 17 #The number of modules in the space station
module = 1 #The module of the space station we are in
last_module = 0 #The last module we were in
possible_moves = [] #List of the possible moves we can make
alive = True #Whether the player is alive or dead
won = False #Whether the player has won
power = 100 #The amount of power the space station has
fuel = 500 #The amount of fuel the player has in the flamethrower
locked = 0 #The module that has been locked by the player
queen = 0 #Location of the queen alien
vent_shafts = [] #Location of the ventilation shaft entrances
info_panels = [] #Location of the information panels
workers = [] #Location of the worker aliens
current_map = "init"
module_info = "init"
targetLoc = "init"
greedy_info_panels = "init"

#Procedure declarations

# this loads the modules. enough said.
def load_module():
    global module, possible_moves, module_info
    possible_moves, module_info = get_modules_from(module)
    output_module()

# we are now reading the text file and adding the data to moves to see where we can move.
def get_modules_from(module):
    moves = []
    text_file = open(str(current_map) + "\\module" + str(module) + ".txt", "r")
    for counter in range(0,4):
        move_read = text_file.readline()
        move_read = int(move_read.strip())
        if move_read != 0:
            moves.append(move_read)

    module_info = text_file.readline().strip()

    text_file.close()
    return moves, module_info

# tells ya what module your in
def output_module():
        global module, module_info
        print()
        print("-----------------------------------------------------------------")
        print()
        print("You are in module",module)
        print(module_info)
        print()

# tells you what moves you can make, with messy base code. again, ugh.
def output_moves():
    global possible_moves
    print()
    print("From here you can move to modules: | ",end='')
    for move in possible_moves:
        print(move,'| ',end='')
        print()

# this gets the actions you can do and allows you to do that action.
def get_action():
    # added power to global variables. woo-hoo.
    global module, last_module, possible_moves, power, targetLoc
    valid_action = False
    while valid_action == False:
        print("What do you want to do next ? (MOVE, SCANNER)")
        action = input(">").strip()
        # jank way of improving input sanitisation and adding stuff
        if action.upper().startswith("MOVE") and len(action) > 4:
            targetLoc = action[4:].strip()
        elif action.upper().startswith("M") and not action.upper().startswith("MOVE") and len(action) > 1:
            targetLoc = action[1:].strip()
        elif action.upper() == "MOVE" or action.upper() == "M":
            targetLoc = input("Enter the module to move to: ").strip()
        if targetLoc != "":
            if targetLoc.isdigit():
                move = int(targetLoc)
                if move in possible_moves:
                    valid_action = True
                    last_module = module
                    module = move
                    # decrementing power by 1 after each move
                    power = power - 1
                else:
                    print("The module must be connected to the current module.")

def loadMap():
    global num_modules, current_map
    map_choice=input("What map do you want to play? (Charles Darwin / Rainbow Omelette): ")
    if map_choice == "Charles Darwin":
        num_modules = 17
        current_map = "Charles_Darwin"
    elif map_choice == "Rainbow Omelette":
        num_modules = 11
        current_map = "Rainbow_Omelette"
    else:
        print("That wasn't a valid map choice, defaulting to Charles Darwin.")
        current_map = "Charles_Darwin"
        num_modules = 17

def spawn_npcs():
    global num_modules, queen, vent_shafts, greedy_info_panels, workers
    module_set = []
    for counter in range(2, num_modules):
        module_set.append(counter)
    random.shuffle(module_set)
    i = 0
    queen = module_set[i]
    for counter in range(0, 3):
        i = i + 1
        vent_shafts.append(module_set[i])

    for counter in range(0, 2):
        i = i + 1
        info_panels.append(module_set[i])

    for counter in range(0, 3):
        i = i + 1
        workers.append(module_set[i])

def rollCredits():
    print("The Great and Powerful bflydev - main programmer")
    print("catgirlshadow (discord) - video wizard consultant")

def printInstructions():
    print("""
    === TELIUM: GAME INSTRUCTIONS ===
    - OBJECTIVE: Find and trap the Queen Alien (Telium) in a module with no exits, then destroy her[cite: 1].
    - MOVES: Type 'MOVE' then enter the module number to navigate adjacent rooms.
    - SCANNER: Type 'SCANNER' then 'LOCK' to lock doors in a room. The Queen cannot enter a locked module.
    - POWER: Moving and using the scanner consumes station power. If power hits 0, you die.
    - HAZARDS: Watch out for worker aliens and ventilation shafts!
    """)

#Main program starts here
def startGame():
    loadMap()
    spawn_npcs()
    print("Queen alien is located in module:", queen)
    print("Ventilation shafts are located in modules:", vent_shafts)
    print("Information panels are located in modules:", info_panels)
    print("Worker aliens are located in modules:", workers)
    global alive, won
    while alive and not won:
        load_module()
        if won == False and alive == True:
            # adding the thing that if you lose all power, you lose and it outputs stuff.
            if power <= 0:
                alive = False
                print("The station has run completely out of power.")
                break
        output_moves()
        get_action()
        if won == True:
            print("The queen is trapped and you burn it to death with your flamethrower.")
            print("Game over. You win!")
        if alive == False:
            print("The station has run out of power. Unable to sustain life support, you die.")

# Title Screen
def homeMenu():
    while 1 < 2:
        print("WELCOME TO TELIUM")
        print("What would you like to do:")
        decision = input("choose: 'play', 'story', 'instructions', 'credits' or 'quit': ")
        if decision == "play":
            startGame()
        elif decision == "story":
            play_video()
        elif decision == "instructions":
            printInstructions()
        elif decision == "quit":
            sys.exit()
        elif decision == "credits":
            rollCredits()
        else:
            print("Uh... I think you did something wrong :(")
