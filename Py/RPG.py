import random
import math
import cutie
import os

#--------------------------------------------------------------------------------------------------------------------------------------
#SKILL CLASS
class Skill():
    skName : str
    skPower : int
    skCost : int
    skType : int #0 - PHYS, 1 - FIRE, 2 - WATER, 3 - ELECTRIC, 4 - WIND, 5 - LIGHT, 6 - DARK, 7 - HEAL
    skDesc : str
    skTarget : int #0 - ENEMY | 1 - ALL ENEMIES | 2 - ALLY | 3 - ALL PARTY | 4 - EVERYONE | 5 - SELF

    def __init__(self, name : str, pow : int, cost : int, type : int, desc : str, target : int):
        self.skName = name
        self.skPower = pow
        self.skCost = cost
        self.skType = type
        self.skDesc = desc
        self.skTarget = target

class SkillCompedium():
    CompleteList : list[Skill] = []

    def add(self, newSkill : Skill):
        self.CompleteList.append(newSkill)


skCompedium = SkillCompedium()
#--------------------------------------------------------------------------------------------------------------------------------------
#BATTLE GUI
class BattleGUI():
    battleRef : Battle
    state : int #0 - START, 1- SKILLSLECT, 2- ITEMSELECT, 3- TARGETSELECT
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
                    if self.battleRef.currChar.currMP > skill.skCost:
                        match skill.skType:
                            case 0:
                                skilloptions.append(f'\x1b[48;5;58m' + f"{skill.skName} - {skill.skCost} MP" + '\x1b[0m')
                            case 1:
                                skilloptions.append(f'\x1b[48;5;160m' + f"{skill.skName} - {skill.skCost} MP" + '\x1b[0m')
                            case 2:
                                skilloptions.append(f'\x1b[48;5;33m' + f"{skill.skName} - {skill.skCost} MP" + '\x1b[0m')
                            case 3:
                                skilloptions.append(f'\x1b[48;5;226m' + f"{skill.skName} - {skill.skCost} MP" + '\x1b[0m')
                            case 4:
                                skilloptions.append(f'\x1b[48;5;34m' + f"{skill.skName} - {skill.skCost} MP" + '\x1b[0m')
                            case 5:
                                skilloptions.append(f'\x1b[48;5;255m' + f"{skill.skName} - {skill.skCost} MP" + '\x1b[0m')
                            case 6:
                                skilloptions.append(f'\x1b[48;5;90m' + f"{skill.skName} - {skill.skCost} MP" + '\x1b[0m')
                            case 7:
                                damaged = False
                                for char in self.battleRef.currTeam:
                                    if char.currHP < char.maxHP:
                                        damaged = True
                                if damaged:
                                    skilloptions.append(f'\x1b[48;5;157m' + f"{skill.skName} - {skill.skCost} MP" + '\x1b[0m')
                            
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
                        print(f'\x1b[48;5;58m' + f"{self.selectedSk.skDesc}" + '\x1b[0m')
                    case 1:
                        print(f'\x1b[48;5;160m' + f"{self.selectedSk.skDesc}" + '\x1b[0m')
                    case 2:
                        print(f'\x1b[48;5;33m' + f"{self.selectedSk.skDesc}" + '\x1b[0m')
                    case 3:
                        print(f'\x1b[48;5;226m' + f"{self.selectedSk.skDesc}" + '\x1b[0m')
                    case 4:
                        print(f'\x1b[48;5;120m' + f"{self.selectedSk.skDesc}" + '\x1b[0m')
                    case 5:
                        print(f'\x1b[48;5;255m' + f"{self.selectedSk.skDesc}" + '\x1b[0m')
                    case 6:
                        print(f'\x1b[48;5;90m' + f"{self.selectedSk.skDesc}" + '\x1b[0m')
                    case 7: 
                        print(f'\x1b[48;5;157m' + f"{self.selectedSk.skDesc}" + '\x1b[0m')
                match self.selectedSk.skTarget:
                    case 0:
                        for enemy in self.battleRef.enemyTeam:
                            enemy.printStats()
                            targetoptions.append(enemy.name)
                    case 1:
                        for enemy in self.battleRef.enemyTeam:
                            enemy.printStats()
                        targetoptions.append("All Enemies")
                    case 2:
                        for ally in self.battleRef.playerTeam:
                            ally.printStats()
                            targetoptions.append(ally.name)
                    case 3:
                        for enemy in self.battleRef.enemyTeam:
                            enemy.printStats()
                        targetoptions.append("All Party")           
                    case 4:
                        for char in self.battleRef.allchar:
                            char.printStats()
                        targetoptions.append("Everyone")
                    case 5:          
                        self.battleRef.currChar.printStats()
                        targetoptions.append(self.battleRef.currChar.name)       
                chosen_idx = cutie.select(targetoptions) -1
                if chosen_idx == -1:
                    self.selectedSk = None
                    self.change_state(0)
                match self.selectedSk.skTarget:
                    case 0:
                        targetlist = [self.battleRef.enemyTeam[chosen_idx]]
                    case 1:
                        targetlist = [self.battleRef.enemyTeam]
                    case 2:
                        targetlist = [self.battleRef.playerTeam[chosen_idx]]
                    case 3:
                        targetlist = [self.battleRef.playerTeam]         
                    case 4:
                        targetlist = [self.battleRef.allchar]
                    case 5:          
                        targetlist = [self.battleRef.currChar] 
                self.battleRef.hit(targetlist, self.selectedSk)
#--------------------------------------------------------------------------------------------------------------------------------------
#CHARACTER CLASS
class Character:
    name : str
    level : int
    xp: int = 0

    state : int = 0 #0 - NONE | 1 - GUARDING

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
    
    def addSkill(self, skill : Skill):
        if len(self.skills) < 7:
            newSkills = self.skills
            newSkills.append(skill)
            self.skills = newSkills


class playerChar(Character):
    remainPoint : int = 8
    xpToLevel : int = 10 

    def levelUP(self):
        self.xp -= self.xpToLevel
        self.level += 1
        self.remainPoint += 3
        self.xpToLevel *= 1.5
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
                    self.remainPoint = points
                    decide = True 

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
                if self.energy <= 0:
                    self.currTeam = self.enemyTeam
                    self.currChar = self.enemyTeam[0]
                    self.energy = len(self.currTeam)
                else:
                    if ((self.currTeam.index(self.currChar) + 1) > len(self.currTeam)-1):
                        self.currChar = self.currTeam[0]
                    else:
                        self.currChar = self.currTeam[self.currTeam.index(self.currChar)+1]
            else:
                if self.energy <= 0:
                    self.currTeam = self.playerTeam
                    self.currChar = self.playerTeam[0]
                    self.energy = len(self.currTeam)
                else:
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
                if self.currChar.currMP < selectSkill.skCost: 
                    self.hit(targetlist, self.currChar.skills[0])
                else:
                    self.hit(targetlist, random.choice(self.currChar.skills))
        self.currChar = None
        self.currTeam = []
        if len(self.enemyTeam) > 0:
            print("You Lose")
            return False
        else:
            print("You Win")
            if self.playerTeam[0].xp > self.playerTeam[0].xpToLevel:
                self.playerTeam[0].levelUP()
            return True


    def hit(self, targetlist : list, skill : Skill):
        self.currChar.currMP -= skill.skCost
        for target in targetlist:
            if skill.skType == 7:
                target.currHP += skill.skPower
                if target.currHP > target.maxHP:
                    target.currHP = target.maxHP
            else:
                if target.state == 1:
                    target.currHP -= skill.skPower/2
                    self.energy -= 1
                else:
                    target.currHP -= skill.skPower
                    self.energy -= 1
            print(f"{self.currChar.name} used {skill.skName} on {target.name}")
        #print(f"{self.energy}")
        if target.currHP <= 0:
            if type(target) == playerChar:
                self.playerTeam.remove(target)
            else:
                self.enemyTeam.remove(target)
                self.currChar.xp += target.xp
                print(f"{target.name} Has been slayed!")
        input()

def createEnemy(name : str) -> Character:
    if player.level < 5:
        minLvl = 1
    else:
        minLvl = player.level - 2
    maxLvl : int = player.level + 2
    selectedLvl : int = random.randrange(minLvl,maxLvl)
    newEnemy = Character(selectedLvl,1,1,1,1,1)

    points : int = ((selectedLvl - 1) * 3) + 8
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
    newEnemy.addSkill(skCompedium.CompleteList[1])
    newEnemy.xp = random.randrange(int(player.xpToLevel * 0.85), int(player.xpToLevel))         
    return newEnemy

os.system('cls' if os.name == 'nt' else 'clear')

skCompedium.add(Skill("Basic Attack", 10, 0, 0, "Deals low physical damage", 0))
skCompedium.add(Skill("Fireball", 20, 10, 1, "Deals low fire damage", 0))
skCompedium.add(Skill("Water Attack", 20, 10, 2, "Deals low water damage", 0))
skCompedium.add(Skill("Static", 20, 10, 3, "Deals low electric damage", 0))
skCompedium.add(Skill("Windmill", 20, 10, 4, "Deals low wind damage", 0))
skCompedium.add(Skill("Blinding Lights", 10, 5, 5, "Deals low light damage", 0))
skCompedium.add(Skill("Darkness", 10, 5, 6, "Deals low dark damage", 0))
skCompedium.add(Skill("Healing", 10, 15, 7, "Heasl a low amount of healt for one ally", 2))


player = playerChar(1,1,1,1,1,1)
player.name = input("Input character name: ")
player.addSkill(skCompedium.CompleteList[1])
player.addSkill(skCompedium.CompleteList[2])
player.addSkill(skCompedium.CompleteList[3])
player.addSkill(skCompedium.CompleteList[4])
player.addSkill(skCompedium.CompleteList[5])
player.addSkill(skCompedium.CompleteList[6])
player.addSkill(skCompedium.CompleteList[7])
player.addSkill(skCompedium.CompleteList[8])
player.printStats()
player.statUP()

inf = True
newbattle = Battle(player)
while inf:
    for a in range(random.randrange(1,3)):
        newbattle.grabEnemy(createEnemy(f"Enemy {a}"))

    inf = newbattle.battle()
