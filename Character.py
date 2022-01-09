
class Character:

    # general initializer
    def __init__(self):

        # Initialize variables
        dummy = -1
        self.__indent = 0

        # int arrays
        self.__stats = []
        self.__mods = []
        self.__saves = []

        # string arrays
        self.__skills = []
        self.__skillMods = []

        # array of stat names
        stats = ["strength", "dexterity", "constitution"]
        stats.append("intelligence")
        stats.append("wisdom")
        stats.append("charisma")

        # array of save names
        saves = ["reflex", "fortitude", "will"]

        for i in range(6):

            # request the stat
            dummy = self.dummyGet(stats[i] + ": ")

            # until the dummy is in the correct range
            while not(isStat(dummy)):

                # request the stat
                dummy = self.dummyGet(stats[i] + ": ")

            # Add the stat to the Integer array
            self.__stats.append(int(dummy))

        # Integer array
        for stat in self.__stats:

            # Configure each mod from the corresponding stat
            mod = int((stat - 10) / 2)

            # account for negative stats
            if stat < 10:
                mod -= 1

            # add the mod to the mod array
            self.__mods.append(int(mod))

        # Integer
        for i in range(3):

            # request the save
            dummy = self.dummyGet(saves[i] + " save bonus: +")

            # until the dummy is in the correct range
            while not(isNat(dummy)):

                # request the save
                dummy = self.dummyGet(saves[i] + " save bonus: +")

            # Add the save to the Integer array
            self.__saves.append(int(dummy))

        # apply mods to save bonuses to get saves
        self.__saves[0] += self.__mods[1]
        self.__saves[1] += self.__mods[2]
        self.__saves[2] += self.__mods[4]

        # request armor bonus
        dummy = self.dummyGet("armor bonus: +")

        while not(isNat(dummy)):

            # request armor bonus
            dummy = self.dummyGet("armor bonus: +")

        self.__armor = int(dummy)

        # request max HP
        dummy = self.dummyGet("max HP: ")

        # until the dummy is in the correct range
        while not(isNat(dummy)):

            # request max HP
            dummy = self.dummyGet("max HP: ")

        # set max hp equal to dummy
        self.__maxHP = int(dummy)

        # Integer
        self.__currHP = self.__maxHP

        # request level
        dummy = self.dummyGet("level: ")

        # until the dummy is in the correct range
        while not(isNat(dummy)):

            # request level
            dummy = self.dummyGet("level: ")

        # Integer
        self.__level = int(dummy)

        # request attack mod
        dummy = self.dummyGet("highest base attack bonus: +")

        # until the dummy is in the correct range
        while not(isNat(dummy)):

            # request attack mod
            dummy = self.dummyGet("highest base attack bonus: +")

        # Integer
        self.__attackMod = int(dummy)

        # Integer
        self.__hitDice = self.__level

        # request hit die
        dummy = self.dummyGet("hit die: d")

        # until the dummy is in the correct range
        while not(isHitDie(dummy)):

            # request hit die
            dummy = input("\n    Please input your hit die: d")

        # Integer
        self.__hitDie = int(dummy)

        # get name: String
        self.__name = self.dummyGet("name: ")

        # get class: String
        self.__class = self.dummyGet("class: ")

        # get race: String
        self.__race = self.dummyGet("race: ")

        print("\n    Please list your skills and their modifiers.")
        print("    Type 'done' when you're done")

        # Request skill
        dummy = input("        skill: ")

        while not(dummy.lower() == "done"):
            # Append to array
            self.__skills.append(dummy)

            # Request skill mod
            dummy = input("\n        " + dummy + " mod: +")

            while not(isNat(dummy)):

                # Request skill mod
                dummy = input("\n        " + dummy + " mod: +")

            # Append to array
            self.__skillMods.append(dummy)

            # Request skill
            dummy = input("\n        skill: ")

    # dummy getter
    def dummyGet(self, var: str) -> str:

        # request given var
        dummy = input("\n    Please input your " + var)

        # return dummy
        return dummy

    def getMaxHP(self) -> int:

        return self.__maxHP

    def getHP(self) -> int:

        return self.__currHP

    def getLevel(self) -> int:

        return self.__level

    def getHitDie(self) -> int:

        return self.__hitDie

    def getHitDice(self) -> int:

        return self.__hitDice

    def getName(self) -> str:

        return self.__name

    def getClass(self) -> str:

        return self.__class

    def getRace(self) -> str:

        return self.__race

    def getAttackMod(self) -> int:

        return self.__attackMod

    def displaySkills(self) -> None:

        # print opening
        print("\n    Skills:")

        # initialize counter
        counter = 0

        for skill in self.__skills:
            print("        " + skill + ": +" + self.__skillMods[counter])

            # increment counter
            counter += 1

        # finish
        return

    def displayStats(self) -> None:

        # initialize variables
        stats = ["Str", "Dex", "Con", "Int", "Wis", "Cha"]
        counter = 0

        # header
        print("\n    Stats:")

        for stat in self.__stats:

            # assign the corrresponding mod
            mod = self.__mods[counter]

            # add + if mod is positive and - if negative
            if mod > 0:
                modText = (" (+" + str(mod) + ")")
            else:
                modText = (" (" + str(mod) + ")")

            print("        " + stats[counter] + ": " + str(stat) + modText)

            # increment counter
            counter += 1

        # finish
        return

    def displayMods(self) -> None:

        # initialize variables
        stats = ["Str", "Dex", "Con", "Int", "Wis", "Cha"]
        counter = 0

        # header
        print("\n    Mods:")

        for mod in self.__mods:
            # add + if mod is positive and - if negative
            if mod > 0:
                modText = ("+" + str(mod))
            else:
                modText = (str(mod))

            # print message
            print("        " + stats[counter] + ": " + modText)

            # increment counter
            counter += 1

            # finish
        return

    def displayAc(self) -> None:

        # initialize variables
        ac = 10 + self.__armor + self.__mods[1]
        touch = 10 + self.__mods[1]
        ff = 10 + self.__armor

        # if dex mod is negative, apply it to the
        # flat-footed AC
        if self.__mods[1] < 0:
            ff -= self.__mods[1]

        # print ac
        print("\n    AC: " + str(ac))
        print("        Touch: " + str(touch))
        print("        Flat-Footed: " + str(ff))

        # finish
        return

    def displayAttacks(self) -> None:

        # initialize variables
        counter = 0
        attackMod = self.__attackMod
        attackText = ["First", "Second", "Third", "Fourth"]

        # for however many attacks the character gets
        while(attackMod > 0):

            # print attack text
            prefix = "    " + attackText[counter] + " attack: +"
            print(prefix + str(attackMod))

            # decrement attackMod
            attackMod -= 5

            # increment counter
            counter += 1

        # print out attack mod if attack mod is zero
        if counter == 0:

            # print attack text
            print("    First attack: +" + str(attackMod))

    def displaySaves(self) -> None:

        # array of save names
        saves = ["Reflex", "Fortitude", "Will"]

        # header
        print("\n    Saves:")

        # initialize counter
        counter = 0

        for save in self.__saves:

            saveText = str(save)

            if save > 0:
                saveText = "+" + saveText

            # print message
            print("\n        " + saves[counter] + ": " + saveText)

            # increment counter
            counter += 1

        # finish
        return

    def displaySheet(self) -> None:

        # initialize variable
        level = str(self.__level)
        currHP = str(self.__currHP)
        maxHP = str(self.__maxHP)
        hitDice = str(self.__hitDice)
        hitDie = str(self.__hitDie)

        # print Name
        print("\n    Name: " + self.__name)

        # print Class
        print("    Class: " + self.__class)

        # print Race
        print("    Race: " + self.__race)

        # print Level
        print("    Level: " + level)

        # print HP
        print("\n    HP: " + currHP + "/" + maxHP)

        # print Hit Dice and Hit Die
        print("    Hit Die: " + hitDice + "d" + hitDie)

        # display stats and mods
        self.displayStats()

        # display ac
        self.displayAc()

        # display skills
        self.displaySkills()

        # finish
        return

    def setHP(self, num: int) -> None:

        # Check if hp is max
        if num >= self.__maxHP:

            # set hp to max
            self.__currHP = self.__maxHP

            # print message
            print("\n    You're at max HP!")

        # Check if hp is zero or below
        elif num <= 0:

            # Check if you're dead
            if num > -self.__stats[2]:

                # set hp
                self.__currHP = num

                # print message
                print("\n    You're dying!")

            else:

                # set hp equal to 0
                self.__currHP = -self.__stats[2]

                print("\n    " + self.__name + " is dead.")

        else:

            # set hp
            self.__currHP = num

        # initialize variables
        currHP = str(self.__currHP)
        maxHP = str(self.__maxHP)

        # print HP
        print("\n    HP: " + currHP + "/" + maxHP)

        # finish
        return

    def setHitDice(self, num: int) -> None:

        # check if hit dice are at max
        # which is equal to character level
        if num > self.__level:

            # set hit dice equal to level
            self.__hitDice = self.__level

        # check if hit dice are zero
        elif num < 0:

            # set hit dice equal to zero
            self.__hitDice = 0

        # initialize variables
        hitDice = str(self.__hitDice)
        hitDie = str(self.__hitDie)

        # print Hit Dice and Hit Die
        print("    Hit Die: " + hitDice + "d" + hitDie)

        # finish
        return


# quick function to check stats
def isStat(dummy: str) -> bool:
    if (dummy.isdigit() and int(dummy) > 0 and int(dummy) <= 20):
        return True
    else:
        # print out error message
        print("    That is not a valid number")

        return False


# quick function to check numbers
def isNat(dummy: str) -> bool:
    if (dummy.isdigit() and int(dummy) >= 0):
        return True

    else:
        # print out error message
        print("    That is not a valid number")

        return False


# checks if hit die are of correct type
def isHitDie(dummy: str) -> bool:

    # Chekc if dummy is a number before casting
    if dummy.isdigit():

        # initialize variables
        temp = int(dummy)

        # check if temp is in the correct values
        if (temp == 6 or temp == 8 or temp == 10 or temp == 12):
            return True

    # print out error message
    print("    That is not a valid hit die value")
    print("    please choose from the following: d6, d8, d10, d12")

    # return false
    return False
