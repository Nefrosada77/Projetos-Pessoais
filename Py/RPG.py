import random
import math
class BattleGUI():
    state : int #0 - START, 1- SKILLSLECT, 2- TARGETSELECT...

    def change_state(self,newState : int):
        self.state = newState
        print()
        match self.state:
            case 0:
                choice : int = 0
                while choice < 1 or choice > 3:
                    print("1- Skills")
                    print("2- Guard")
                    print("3- Run")
                    choice = int(input("Select: "))
                    match choice:
                        case 1:
                            self.change_state(1)
                        case 2:
                            print("Guarded")
                        case 3:
                            print("Quit")
            case 1:
                print("1- Back")
                print("2- SKILL1")
                print("3- SKILL2")
                choice = int(input("Select: "))
                if choice == 1:
                    self.change_state(0) 

class Character:
    name : str
    level : int
    xp: int = 0

    #MAX AND CURRENT HP AND MP
    maxHP : int
    currHP : int
    maxMP : int
    currMP : int

    #STATS - level 100 = 305
    strength : int
    magic : int
    resistance : int
    agility : int
    luck : int
    
    def __init__(self,lvl, str, mag, res, agi, luck):
        self.level = lvl
        self.strength = str
        self.magic = mag
        self.resistance = res
        self.agility = agi
        self.luck = luck
        self.maxHP = int(10 * (math.sqrt(self.level) + self.resistance//2))
        self.currHP = self.maxHP
        self.maxMP = int(10 * (math.sqrt(self.level) + math.sqrt(self.magic*3))) #TODO ACHAR EQUAÇÃO PERFEITA PARA MANA - LVL 1 | MAG 10 = 50MP // LVL100 | MAG 160 = 650MP
        self.currMP = self.maxMP

    def updateStats(self, newStr, newMag, newRes, newAgi, newLuck):
        self.strength += newStr
        self.magic += newMag
        self.resistance += newRes
        self.agility += newAgi
        self.luck += newLuck
        self.maxHP = int(10 * (math.sqrt(self.level) + self.resistance//2))
        self.currHP = self.maxHP
        self.maxMP = int(10 * ((math.sqrt(self.level)/7 * math.sqrt(self.magic)/5))/10)
        self.currMP = self.max
    
    def getStr(self):
        return self.strength

    def getMag(self):
        return self.magic

    def getRes(self):
        return self.resistance

    def getAgil(self):
        return self.agility

    def getLuck(self):
        return self.luck 

    def printStats(self):
        print("------------------------")
        print(f"{self.name} - Level {self.level}")
        print(f"HP - {self.currHP}/{self.maxHP}")
        print(f"MP - {self.currMP}/{self.maxMP}")
        print()
        print(f"Strength - {self.strength}")
        print(f"Magic - {self.magic}")
        print(f"Resistence - {self.resistance}")
        print(f"Agility - {self.agility}")
        print(f"Luck - {self.luck}")
        print("------------------------")    

class StrongMan100(Character):
    
    def __init__(self):
        super().__init__(100,100,20,85,60,40) #0 / 305
        self.name = "STRONGMAN100"

class MagicMan100(Character):

    def __init__(self):
        super().__init__(100,20,160,45,60,20) #0 /305
        self.name = "MAGICMAN100"

class StrongMan50(Character):
    
    def __init__(self):
        super().__init__(50,50,10,45,35,15) #0 /155
        self.name = "STRONGMAN50"

class MagicMan50(Character):

    def __init__(self):
        super().__init__(50,10,50,30,55,10) #0 /155
        self.name = "MAGICMAN50"

class StrongMan10(Character):
    
    def __init__(self):
        super().__init__(10,10,4,9,7,5) #0 /35
        self.name = "STRONGMAN10"

class MagicMan10(Character):

    def __init__(self):
        super().__init__(10,4,10,9,9,3) #0 / 35
        self.name = "MAGICMAN10"

class playerChar(Character):
    remainPoint : int = 8
    xpToLevel : int = 10
    gui : BattleGUI = BattleGUI()

    def levelUP(self):
        self.xp -= self.xpToLevel
        self.level += 1
        self.remainPoint += 3
        self.xpToLevel *= 1.5

class Battle():
    playerTeam : list[Character] = []
    enemyTeam : list[Character] = []
    currTeam : list[Character] = []
    currChar : Character = None
    energy : int = 0

    def __init__(self, player):
        self.playerTeam.append(player)
    
    def grabEnemie(self,enemy : Character):
        self.enemyTeam.append(enemy)

    def battle(self):
        if self.currChar == None:
            self.currTeam = self.playerTeam
            self.currChar = self.playerTeam[0]
            self.energy = len(self.playerTeam)
        while player.currHP > 0 or (char.currHP > 0 for char in self.enemyTeam):
            if self.energy <= 0:
                if self.currTeam == self.playerTeam:
                    self.currTeam = self.enemyTeam
                    self.currChar = self.enemyTeam[0]
                else:
                    self.currTeam = self.playerTeam
                    self.currChar = self.playerTeam[0]
            self.energy = len(self.currTeam)
            if self.currChar == player:
                player.gui.change_state(0)    


    def hit(self, target):
        target

'''
player = playerChar(1,1,1,1,1,1)
player.name = input("Input character name: ")
decide : bool = False
player.printStats()

enemy = StrongMan10()

while not decide:
    print(f"Remaning Points: {player.remainPoint}")
    newStr = int(input("Add Strength: "))
    newMag = int(input("Add Magic: "))
    newRes = int(input("Add Resistance: "))
    newAgi = int(input("Add Agility: "))
    newLuck = int(input("Add Luck: "))
    pointUsed = newStr + newMag + newRes + newAgi + newLuck 
    if (newStr, newMag, newRes, newAgi, newLuck > 1) and (pointUsed) == player.remainPoint:
        player.updateStats(newStr, newMag, newRes, newAgi, newLuck)
        player.printStats()
        next = input("Continue (Y/N): ")
        options = ["Y", "y", "YES", "Yes", "YEs", "YeS", "yEs", "yES", "yeS"]
        if next in options:
            player.remainPoint = 0
            decide = True

inf = Battle(player)
inf.grabEnemie(enemy)
inf.battle()
'''
char1 = StrongMan100()
char1.printStats()
char2 = StrongMan50()
char2.printStats()
char3 = StrongMan10()
char3.printStats()

char1 = MagicMan100()
char1.printStats()
char2 = MagicMan50()
char2.printStats()
char3 = MagicMan10()
char3.printStats()