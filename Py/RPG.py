import random
import math
import cutie
import os
import csv

#--------------------------------------------------------------------------------------------------------------------------------------
#SKILL CLASS
class Skill():
    skName : str
    skPower : int
    skCost : int
    skType : int #0 - PHYS, 1 - FIRE, 2 - WATER, 3 - ELECTRIC, 4 - WIND, 5 - LIGHT, 6 - DARK, 7 - HEAL
    skDesc : str
    skTarget : int #0 - ENEMY | 1 - ALL ENEMIES | 2 - ALLY | 3 - ALL PARTY | 4 - EVERYONE | 5 - SELF
    skLevel : int

    def __init__(self, name : str, pow : int, cost : int, type : int, desc : str, target : int, level: int):
        self.skName = name
        self.skPower = pow
        self.skCost = cost
        self.skType = type
        self.skDesc = desc
        self.skTarget = target
        self.skLevel = level


class SkillCompedium():
    CompleteList : list[Skill] = []

    def add(self, newSkill : Skill):
        self.CompleteList.append(newSkill)


skCompedium = SkillCompedium()
#--------------------------------------------------------------------------------------------------------------------------------------
#BATTLE GUI
class BattleGUI():
    battleRef : Battle
    state : int #0- START | 1- SKILLSLECT | 2- ITEMSELECT | 3- TARGETSELECT | 4- CHANGE SKILLS | 5- SELECT SKILL TO CHANGE
    selectedSk : Skill
    

    def __init__(self, battle):
        self.battleRef = battle

    def change_state(self,newState : int):
        self.state = newState
        match self.state:
            case 0: #START MENU
                os.system('cls' if os.name == 'nt' else 'clear')
                startoptions = ["Skills", "Guard", "Analyse"]
                print(f"Number of actions: {self.battleRef.energy}")
                self.battleRef.currChar.printStats()
                chosen_idx = cutie.select(startoptions)
                match chosen_idx:
                    case 0:
                        self.change_state(1)
                    case 1:
                        self.battleRef.currChar.state = 1
                        self.battleRef.energy -= 1
                    case 2:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        for char in self.battleRef.enemyTeam:
                            char.printStats()
                        input()
            case 1: #SKILL MENU
                os.system('cls' if os.name == 'nt' else 'clear')
                skilloptions = ["Back"]
                for skill in self.battleRef.currChar.skills:
                    if self.battleRef.currChar.currMP >= skill.skCost:
                        match skill.skType:
                            case 0:
                                skilloptions.append(f'\x1b[48;5;58m' + f'\x1b[38;5;15m' + f"{skill.skName} - {skill.skCost} MP " + '\x1b[0m')
                            case 1:
                                skilloptions.append(f'\x1b[48;5;160m' + f'\x1b[38;5;15m'  + f"{skill.skName} - {skill.skCost} MP " + '\x1b[0m')
                            case 2:
                                skilloptions.append(f'\x1b[48;5;33m' + f'\x1b[38;5;15m' + f"{skill.skName} - {skill.skCost} MP " + '\x1b[0m')
                            case 3:
                                skilloptions.append(f'\x1b[48;5;226m' + f'\x1b[38;5;0m' + f"{skill.skName} - {skill.skCost} MP " + '\x1b[0m')
                            case 4:
                                skilloptions.append(f'\x1b[48;5;34m' + f'\x1b[38;5;15m' + f"{skill.skName} - {skill.skCost} MP " + '\x1b[0m')
                            case 5:
                                skilloptions.append(f'\x1b[48;5;255m' + f'\x1b[38;5;0m' + f"{skill.skName} - {skill.skCost} MP " + '\x1b[0m')
                            case 6:
                                skilloptions.append(f'\x1b[48;5;90m' + f'\x1b[38;5;15m' + f"{skill.skName} - {skill.skCost} MP " + '\x1b[0m')
                            case 7:
                                damaged = False
                                for char in self.battleRef.currTeam:
                                    if char.currHP < char.maxHP:
                                        damaged = True
                                if damaged:
                                    skilloptions.append(f'\x1b[48;5;157m' + f'\x1b[38;5;0m' + f"{skill.skName} - {skill.skCost} MP " + '\x1b[0m')
                            
                chosen_idx = cutie.select(skilloptions) - 1
                if chosen_idx == -1:
                    self.selectedSk = None
                    self.change_state(0)
                else:
                    self.selectedSk = self.battleRef.currChar.skills[chosen_idx]
                    self.change_state(3)
            case 2: #ITEM MENU
                pass
            case 3: #TARGET MENU
                os.system('cls' if os.name == 'nt' else 'clear')
                targetoptions = ["Back"]
                match self.selectedSk.skType:
                    case 0:
                        print(f'\x1b[48;5;58m' + f'\x1b[38;5;15m' + f"{self.selectedSk.skDesc}" + '\x1b[0m')
                    case 1:
                        print(f'\x1b[48;5;160m' + f'\x1b[38;5;15m' + f"{self.selectedSk.skDesc}" + '\x1b[0m')
                    case 2:
                        print(f'\x1b[48;5;33m' + f'\x1b[38;5;15m' + f"{self.selectedSk.skDesc}" + '\x1b[0m')
                    case 3:
                        print(f'\x1b[48;5;226m' + f'\x1b[38;5;0m' + f"{self.selectedSk.skDesc}" + '\x1b[0m')
                    case 4:
                        print(f'\x1b[48;5;120m' + f'\x1b[38;5;15m' + f"{self.selectedSk.skDesc}" + '\x1b[0m')
                    case 5:
                        print(f'\x1b[48;5;255m' + f'\x1b[38;5;0m' + f"{self.selectedSk.skDesc}" + '\x1b[0m')
                    case 6:
                        print(f'\x1b[48;5;90m' + f'\x1b[38;5;15m' + f"{self.selectedSk.skDesc}" + '\x1b[0m')
                    case 7: 
                        print(f'\x1b[48;5;157m' + f'\x1b[38;5;0m' + f"{self.selectedSk.skDesc}" + '\x1b[0m')
                match self.selectedSk.skTarget:
                    case 0:
                        for enemy in self.battleRef.enemyTeam:
                            enemy.printHPMP()
                            targetoptions.append(enemy.name)
                    case 1:
                        for enemy in self.battleRef.enemyTeam:
                            enemy.printHPMP()
                        targetoptions.append("All Enemies")
                    case 2:
                        for ally in self.battleRef.playerTeam:
                            ally.printStats()
                            targetoptions.append(ally.name)
                    case 3:
                        for enemy in self.battleRef.enemyTeam:
                            enemy.printHPMP()
                        targetoptions.append("All Party")           
                    case 4:
                        for char in self.battleRef.allchar:
                            enemy.printHPMP()
                        targetoptions.append("Everyone")
                    case 5:          
                        self.battleRef.currChar.printHPMP()
                        targetoptions.append(self.battleRef.currChar.name)       
                chosen_idx = cutie.select(targetoptions) -1
                if chosen_idx == -1:
                    self.selectedSk = None
                    self.change_state(0)
                else:
                    match self.selectedSk.skTarget:
                        case 0:
                            targetlist = [self.battleRef.enemyTeam[chosen_idx]]
                        case 1:
                            targetlist = self.battleRef.enemyTeam
                        case 2:
                            targetlist = [self.battleRef.playerTeam[chosen_idx]]
                        case 3:
                            targetlist = self.battleRef.playerTeam
                        case 4:
                            targetlist = self.battleRef.allchar
                        case 5:      
                            targetlist = [self.battleRef.currChar]
                    self.battleRef.hit(targetlist, self.selectedSk)
            case 4: #CHANGE SKILLS MENU
                os.system('cls' if os.name == 'nt' else 'clear')
                skilloptions = []
                print("Your Skills: ")
                for skill in self.battleRef.playerTeam[0].skills:
                    if skill.skName != "Basic Attack":
                        match skill.skType:
                            case 0:
                                print(f'\x1b[48;5;58m' + f'\x1b[38;5;15m' + f"{skill.skName} - {skill.skCost} MP | {skill.skDesc}" + '\x1b[0m')
                            case 1:
                                print(f'\x1b[48;5;160m' + f'\x1b[38;5;15m' + f"{skill.skName} - {skill.skCost} MP | {skill.skDesc}" + '\x1b[0m')
                            case 2:
                                print(f'\x1b[48;5;33m' + f'\x1b[38;5;15m' + f"{skill.skName} - {skill.skCost} MP | {skill.skDesc}" + '\x1b[0m')
                            case 3:
                                print(f'\x1b[48;5;226m' + f'\x1b[38;5;0m' + f"{skill.skName} - {skill.skCost} MP | {skill.skDesc}" + '\x1b[0m')
                            case 4:
                                print(f'\x1b[48;5;34m' + f'\x1b[38;5;15m' + f"{skill.skName} - {skill.skCost} MP | {skill.skDesc}" + '\x1b[0m')
                            case 5:
                                print(f'\x1b[48;5;255m' + f'\x1b[38;5;0m' + f"{skill.skName} - {skill.skCost} MP | {skill.skDesc}" + '\x1b[0m')
                            case 6:
                                print(f'\x1b[48;5;90m' + f'\x1b[38;5;15m' + f"{skill.skName} - {skill.skCost} MP | {skill.skDesc}" + '\x1b[0m')
                            case 7:
                                print(f'\x1b[48;5;157m' + f'\x1b[38;5;0m' + f"{skill.skName} - {skill.skCost} MP | {skill.skDesc}" + '\x1b[0m')
                print("\nSelect a skill to put in your inventory:")
                for skill in skCompedium.CompleteList:
                    if skill.skName != "Basic Attack":
                        if skill.skLevel <= self.battleRef.playerTeam[0].level:
                            match skill.skType:
                                case 0:
                                    skilloptions.append(f'\x1b[48;5;58m' + f'\x1b[38;5;15m' + f"{skill.skName} - {skill.skCost} MP | {skill.skDesc}" + '\x1b[0m') 
                                case 1:
                                    skilloptions.append(f'\x1b[48;5;160m' + f'\x1b[38;5;15m' + f"{skill.skName} - {skill.skCost} MP | {skill.skDesc}" + '\x1b[0m') 
                                case 2:
                                    skilloptions.append(f'\x1b[48;5;33m' + f'\x1b[38;5;15m' + f"{skill.skName} - {skill.skCost} MP | {skill.skDesc}" + '\x1b[0m') 
                                case 3:
                                    skilloptions.append(f'\x1b[48;5;226m' + f'\x1b[38;5;0m' + f"{skill.skName} - {skill.skCost} MP | {skill.skDesc}" + '\x1b[0m') 
                                case 4:
                                    skilloptions.append(f'\x1b[48;5;34m' + f'\x1b[38;5;15m' + f"{skill.skName} - {skill.skCost} MP | {skill.skDesc}" + '\x1b[0m') 
                                case 5:
                                    skilloptions.append(f'\x1b[48;5;255m' + f'\x1b[38;5;0m' + f"{skill.skName} - {skill.skCost} MP | {skill.skDesc}" + '\x1b[0m') 
                                case 6:
                                    skilloptions.append(f'\x1b[48;5;90m' + f'\x1b[38;5;15m' + f"{skill.skName} - {skill.skCost} MP | {skill.skDesc}" + '\x1b[0m') 
                                case 7:
                                    skilloptions.append(f'\x1b[48;5;157m' + f'\x1b[38;5;0m' + f"{skill.skName} - {skill.skCost} MP | {skill.skDesc}" + '\x1b[0m') 
                skilloptions.append("Continue")
                chosen_idx = cutie.select(skilloptions)
                if chosen_idx == len(skilloptions)-1:
                    return
                else:
                    self.selectedSk = skCompedium.CompleteList[chosen_idx+1]
                    self.change_state(5)
            case 5: #SELECT SLOT TO CHANGE MENU
                print()
                skilloptions = []                     
                for idx in range(1,9):
                    try: 
                        skilloptions.append(self.battleRef.playerTeam[0].skills[idx].skName)
                    except:
                        skilloptions.append("Empty")
                skilloptions.append("Back")
                chosen_idx = cutie.select(skilloptions)
                if chosen_idx < 9:
                    if len(self.battleRef.playerTeam[0].skills) >= 9:
                        self.battleRef.playerTeam[0].replaceSkill(self.selectedSk, chosen_idx+1)
                    else:
                        self.battleRef.playerTeam[0].addSkill(self.selectedSk)
                    self.change_state(4)
                else:
                    self.change_state(4)

#--------------------------------------------------------------------------------------------------------------------------------------
#CHARACTER CLASS
class Character:
    name : str = None
    level : int = 1
    xp: int = 0

    state : int = 0 #0 - NONE | 1 - GUARDING

    #MAX AND CURRENT HP AND MP
    maxHP : int
    currHP : int
    maxMP : int
    currMP : int

    #AFFINITIES
    weakness : list = []
    resist : list = []
    block : list = []
    drain : list = []
    repel : list = []

    #STATS | level 100 = 305
    strength : int
    magic : int
    resistance : int
    agility : int
    luck : int

    #SKILLS
    skills : list[Skill] = []
    
    def __init__(self,lvl, str, mag, res, agi, luck):
        self.level = lvl
        self.strength = str
        self.magic = mag
        self.resistance = res
        self.agility = agi
        self.luck = luck
        self.maxHP = int(10 * (math.sqrt(self.level) + self.resistance//2))
        self.currHP = self.maxHP
        self.maxMP = int(10 + 1 * (self.level * 2 + self.magic *3))
        self.currMP = self.maxMP
        self.skills = [skCompedium.CompleteList[0]]

    def updateHPMP(self):
        self.maxHP = int(10 * (math.sqrt(self.level) + self.resistance//2))
        self.currHP = self.maxHP
        self.maxMP = int(10 + 1 * (self.level * 2 + self.magic *3))
        self.currMP = self.maxMP
    
    def resetState(self):
        self.state = 0

    def printStats(self):
        print("------------------------")
        print(f"{self.name} | Level {self.level}")
        print("------------------------")        
        print(f"HP - {self.currHP}/{self.maxHP}")
        print(f"MP - {self.currMP}/{self.maxMP}\n")
        print(f"Strength - {self.strength}")
        print(f"Magic - {self.magic}")
        print(f"Resistence - {self.resistance}")
        print(f"Agility - {self.agility}")
        print(f"Luck - {self.luck}")
        print("------------------------")    
    
    def printHPMP(self):
        print("------------------------")
        print(f"{self.name} | Level {self.level}")
        print("------------------------")        
        print(f"HP - {self.currHP}/{self.maxHP}")
        print(f"MP - {self.currMP}/{self.maxMP}")
        print("------------------------")   
    
    def addSkill(self, skill : Skill):
        if not skill in self.skills:
            if len(self.skills) < 9:
                newSkills = self.skills
                newSkills.append(skill)
                self.skills = newSkills

    def replaceSkill(self, newSkill : Skill, replaceIdx : int):
        newSkills = self.skills
        newSkills[replaceIdx] = newSkill
        self.skills = newSkills


class playerChar(Character):
    remainPoint : int = 8
    xpToLevel : int = 10 

    def levelUP(self):
        self.xp -= self.xpToLevel
        self.level += 1
        self.remainPoint += 3
        self.xpToLevel *= 1.5
        for skill in skCompedium.CompleteList:
            if skill.skLevel == self.level:
                print(f"Unlocked new skill -> {skill.skName}")
        input()
        self.statUP()
    
    def statUP(self):
        decide : bool = False
        points : int = self.remainPoint
        statsoptions = ["Strength","Magic","Resistence","Agility","Luck"]
        while not decide:
            prevStr = self.strength
            prevMag = self.magic
            prevRes = self.resistance
            prevAgi = self.agility
            prevLuck = self.luck
            while points > 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.updateHPMP()
                self.printStats()
                print(f"Remaning Points: {points}")
                print(f"Choose a atribute to level up: ")
                choise_idx = cutie.select(statsoptions)
                match choise_idx:
                    case 0:
                        self.strength += 1
                    case 1:
                        self.magic += 1
                    case 2:
                        self.resistance += 1
                    case 3:
                        self.agility += 1
                    case 4: 
                        self.luck += 1
                points -= 1
            os.system('cls' if os.name == 'nt' else 'clear')
            self.updateHPMP()
            self.printStats()
            options = ["NO","YES"]
            print("Continue: ")
            choise_idx = cutie.select(options)
            match choise_idx:
                case 0:
                    points = self.remainPoint
                    self.strength = prevStr
                    self.magic = prevMag
                    self.resistance = prevRes
                    self.agility = prevAgi
                    self.luck = prevLuck
                case 1:
                    self.remainPoint = 0
                    decide = True 
    
    def changeSkills(self):
        newbattle.gui.change_state(4)

#--------------------------------------------------------------------------------------------------------------------------------------
#BATTLE
class Battle():
    gui : BattleGUI
    playerTeam : list[Character] = []
    enemyTeam : list[Character] = []
    allchar : list[Character] = []
    currTeam : list[Character] = []
    currChar : Character = None
    energy : int = 0

    def __init__(self,player):
        self.playerTeam.append(player)
        self.gui = BattleGUI(self)
    
    def grabEnemy(self,enemy : Character):
        self.enemyTeam.append(enemy)

    def battle(self) -> bool:
        self.allchar = self.playerTeam + self.enemyTeam
        self.playerTeam[0].updateHPMP()
        if self.currChar == None:
            self.currChar = self.playerTeam[0]
            self.currTeam = self.playerTeam
            self.energy = len(self.playerTeam)
        while len(self.playerTeam) > 0 and len(self.enemyTeam) > 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            for char in self.allchar:
                char.resetState()
            if self.currTeam == self.playerTeam: 
                if self.energy <= 0: #PASS TURN TO THE ENEMY TEAM
                    self.currTeam = self.enemyTeam
                    self.currChar = self.enemyTeam[0]
                    self.energy = len(self.currTeam)
                else: #CHANGE PLAYER TEAM TURN
                    if ((self.currTeam.index(self.currChar) + 1) > len(self.currTeam)-1):
                        self.currChar = self.currTeam[0]
                    else:
                        self.currChar = self.currTeam[self.currTeam.index(self.currChar)+1]
            else:
                if self.energy <= 0: #PASS TURN TO THE PLAYER TURN
                    self.currTeam = self.playerTeam
                    self.currChar = self.playerTeam[0]
                    self.energy = len(self.currTeam)
                else: #CHANGE ENEMY TEAM TURN
                    if ((self.currTeam.index(self.currChar) + 1) > len(self.currTeam)-1):
                        self.currChar = self.currTeam[0]
                    else:
                        self.currChar = self.currTeam[self.currTeam.index(self.currChar)+1]
            
            if self.currChar == player: #PLAYER TURN
                self.gui.change_state(0)    
            else: #ENEMY TURN
                selectSkill = random.choice(self.currChar.skills)
                match selectSkill.skType:
                    case 0:
                        targetlist = [random.choice(self.playerTeam)]
                    case 1:
                        targetlist = self.playerTeam
                    case 2:
                        targetlist = [random.choice(self.enemyTeam)]
                    case 3:
                        targetlist = self.enemyTeam      
                    case 4:
                        targetlist = self.allchar
                    case 5:          
                        targetlist = [self.currChar]
                self.hit(targetlist, selectSkill)
        self.currChar = None
        self.currTeam = []
        if len(self.enemyTeam) > 0:
            return False
        else:
            self.playerTeam[0].xp += random.randrange(int(self.playerTeam[0].xpToLevel * 0.85), int(self.playerTeam[0].xpToLevel))
            while self.playerTeam[0].xp > self.playerTeam[0].xpToLevel:
                self.playerTeam[0].levelUP()
            return True


    def hit(self, targetlist : list[Character], skill : Skill):
        self.currChar.currMP -= skill.skCost
        damage : int = skill.skPower
        energyUsed : int = 1
        for target in targetlist:
            if skill.skType in target.repel:
                target = self.currChar
                energyUsed = self.energy
            if target.state == 1 or skill.skType in target.resist:
                damage /= 2
            if skill.skType in target.weakness:
                damage *= 2
                energyUsed = 0.5
            if skill.skType in target.drain or skill.skType == 7:
                damage *= -1
                energyUsed = self.energy
            if skill.skType in target.block:
                damage = 0
                energyUsed = 2
            target.currHP -= damage
            if target.currHP > target.maxHP:
                target.currHP = target.maxHP
            self.energy -= energyUsed
            print(f"{self.currChar.name} used {skill.skName} on {target.name}")
        #print(f"{self.energy}")
        if target.currHP <= 0:
            if type(target) == playerChar:
                self.playerTeam.remove(target)
            else:
                self.enemyTeam.remove(target)
                print(f"{target.name} Has been slayed!")
        input()


def createEnemy(name : str, level: int) -> Character:
    #TODO CREATE A TABLE WITH DIFERENT PRESETS FOR ENEMIES
    newEnemy = Character(level,1,1,1,1,1)
    points : int = ((level - 1) * 3) + 8
    newEnemy.name = name
    for point in range(points):
        stat = random.randrange(0,4)
        match stat:
            case 0:
                newEnemy.strength += 1
            case 1:
                newEnemy.magic += 1
            case 2:
                newEnemy.resistance += 1
            case 3:
                newEnemy.agility += 1
            case 4:
                newEnemy.luck += 1
    newEnemy.updateHPMP()        
    return newEnemy

os.system('cls' if os.name == 'nt' else 'clear')
#--------------------------------------------------------------------------------------------------------------------------------------
#SKILL CREATION
def createSkill(name : str, pow : int, cost : int, type : int, desc : str, target : int, level: int):
    skCompedium.add(Skill(name, pow, cost, type, desc, target, level))

compediumFile = "skCompedium.csv"
fields = []
rows = []

with open(compediumFile, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    
for row in rows:
    createSkill(row[0], int(row[1]), int(row[2]), int(row[3]), row[4], int(row[5]), int(row[6]))

for skill in skCompedium.CompleteList:
    #print(skill.skName)
    pass

player = playerChar(1,1,1,1,1,1)
while player.name == None or (len(player.name) < 3 or len(player.name) > 15):
    player.name = input("Input character name: ")
    if len(player.name) < 3:
        print("Name's too short")
    if len(player.name) > 15:
        print("Name's too long")
player.printStats()
player.addSkill(skCompedium.CompleteList[1])
player.addSkill(skCompedium.CompleteList[2])
player.addSkill(skCompedium.CompleteList[3])
player.addSkill(skCompedium.CompleteList[4])
player.addSkill(skCompedium.CompleteList[5])
player.addSkill(skCompedium.CompleteList[6])
player.addSkill(skCompedium.CompleteList[7])
player.statUP()

inf = True
newbattle = Battle(player)
while inf:
    newbattle.grabEnemy(createEnemy(f"Enemy {len(newbattle.enemyTeam)}", player.level))
        
    inf = newbattle.battle()
    if inf:
        player.changeSkills()
