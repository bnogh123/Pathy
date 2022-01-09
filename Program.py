from Character import *

def main() -> None:

    # Initialize Variables
    command = "null"

    # Print welcome message
    print()
    print("Hello! I'm Pathy, your pathfinder assistant!")
    print("Let's make your character.")

    # create player
    player = Character()

    # prints message
    print("\n    Pathy will start out of combat")

    # goes until the command is end
    while not(isEnd(command)):

        # get command
        command = getCommand()

        # check if the command is for combat
        if not(isCombat(command)):

            # call out of combat and store output in flag
            isCorrect = outOfCombat(player, command)

            # check for error message
            if not(isCorrect) and not(isEnd(command)):

                # print error messsage
                print("    That is not a valid command")

        else:

            # print message
            print("\n    Beginning combat...")

            # call combat
            combat(player)

            # print message
            print("\n    Congrats! You survived combat!")

def toNat(num: str) -> int:

    # check if num is a natural number
    if num.isdigit() and int(num) > 0:

        # if so, return it
        return int(num)

    else:

        # if not, or if equal to zero, return zero
        return 0

def isCombat(com: str) -> bool:

    # check if com is end or not
    if com.lower() == "combat":
        return True

    else:
        return False

def isEnd(com: str) -> bool:

    # check if com is end or not
    if com.lower() == "end":
        return True

    else:
        return False


def getCommand() -> str:

    # display commands
    displayCommands()

    # get command
    command = input("\n    Please input a command\n\t")

    # return command
    return command

def displayCommands() -> None:

    print("\n    Commands:")

    print("        Sheet")
    print("        Heal")
    print("        Damage")
    print("        Skill")
    print("        Save")
    print("        Flat")
    print("        Help")
    print("        Combat")
    print("        End")

    # only available in combat
    print("\n    In combat:")
    print("        Attack")

    return

def displayHelp() -> None:

    print("\n    Commands:")

    print("        Sheet- displays character sheet")
    print("        Heal- character regains hp")
    print("        Damage- character takes damage")
    print("        Skill- displays skills")
    print("        Save- displays saves")
    print("        Flat- displays flat modifiers")
    print("        Help- displays commands")
    print("        Combat- starts combat")
    print("        End- closes pathy if out of combat")

    return


# enacts combat
def combat(player: Character) -> None:

    # prompt for command
    print("\n    Enter damage taken, End if ")
    print("    combat is over, or Go if you ")
    command = input("    would instead like to act\n\t")

    # check if they entered a damage amount taken
    if command.isdigit() and int(command) > 0:

        # take the damage
        newHP = player.getHP() - int(command)
        player.setHP(newHP)

        # recursively call combat
        combat(player)

    elif command.lower() == "go":

        # call a turn in combat
        # and set a flag variable isCombat
        turn(player)

        # recursively call combat
        combat(player)

    elif command.lower() != "end":

        # print error message
        print("\n    That is not a valid command")

        # recursively call combat
        combat(player)

    # return, ending combat and any recursive calling
    return

# enacts a turn
def turn(player: Character) -> None:

    # gets new command
    command = getCommand()

    # checks if the command is
    # an out of combat command
    isOOC = outOfCombat(player, command)

    if isOOC:

        # checks if the command is
        # to display help commands
        if command.lower() == "help":

            # prints the other commands that can
            # be done in combat
            print("\n    In combat:")
            print("        Attack- gives base attack bonus")

        # this is to prevent combat
        # from not ending due to recursion
        isOOC = False

    # checks if the player wants to attack
    elif command.lower() == "attack":

        # call function
        player.displayAttacks()

    else:

        # prints error message
        print("\n    That is not a valid command")

    # returns
    return

# returns true if com is a valid
# out of combat command, otherwise returs false
def outOfCombat(player: Character, com: str) -> bool:

    # check for all cases
    if com.lower() == "sheet":

        # display the player's sheet
        player.displaySheet()

        # return true to indicate that
        # a specified action was executed
        return True

    elif com.lower() == "heal":

        # prompt user for hit points healed
        dummy = input("\n    How many hit points would you like to heal?\n\t")

        # find new hp and set
        dummy = player.getHP() + toNat(dummy)
        player.setHP(dummy)

        # prompt user for hit dice used
        dummy = input("\n    How many hit die were used?\n\t")

        # find new hit dice and set
        dummy = player.getHitDice() - toNat(dummy)
        player.setHitDice(dummy)

        # return true to indicate that
        # a specified action was executed
        return True

    elif com.lower() == "damage":

        # prompt user for damage taken
        dummy = input("\n    How many points of damage did you take?\n\t")

        # find new hp and set
        dummy = player.getHP() - toNat(dummy)
        player.setHP(dummy)

        # return true to indicate that
        # a specified action was executed
        return True

    elif com.lower() == "skill":

        # display skills
        player.displaySkills()

        # return true to indicate that
        # a specified action was executed
        return True

    elif com.lower() == "save":

        # display saves
        player.displaySaves()

        # return true to indicate that
        # a specified action was executed
        return True

    elif com.lower() == "flat":

        # display modifiers
        player.displayMods()

        # return true to indicate that
        # a specified action was executed
        return True

    elif com.lower() == "help":

        # display help commands
        displayHelp()

        # return true to indicate that
        # a specified action was executed
        return True

    else:

        return False


# Call the main function
main()
