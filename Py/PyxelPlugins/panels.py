import pyxel as py
import skills as sk

WIDTH = 400
HEIGHT = 240

class Double():
    x : int
    y : int

    def __init__(self, value : tuple):
        self.x = value[0]
        self.y = value[1]

class Panel():
    size : Double
    position : Double
    color : int

    def __init__(self, x : int, y : int, width : int, height : int, color : int):
        self.size = Double([width, height])
        self.position = Double([x,y])
        self.color = color
    
    def draw(self):
        py.rect(self.position.x-(self.size.x/2),self.position.y-(self.size.y/2), #POSITION
                self.size.x,self.size.y, #SIZE
                self.color) #COLOR

class ListPanel(Panel):
    items : list
    selector : int = 0
    textColor : int
    margin : int
    space : int 

    def __init__(self, x : int, y : int, width : int, items : list, panel_color : int = py.COLOR_WHITE, text_color : int = py.COLOR_BLACK, margin : int = 8, space : int = 4):
        self.items = items
        self.textColor = text_color
        self.margin = margin
        self.space = space
        if type(self.items[0]) == sk.Skill:
            for i in range(len(self.items)):
                if i < len(self.items):
                    if self.items[i].type == sk.Type.AUTO:
                        self.items.pop(i)
    
        super().__init__(x, y, width+(margin)-1, (len(self.items)*py.FONT_HEIGHT) + (margin) + (space*(len(self.items)-1))-1, panel_color)
    
    def draw(self):
        super().draw()
        for i in range(len(self.items)):
            if type(self.items[i]) == str:
                py.text((self.position.x - (self.size.x/2)) + (self.margin/2) + 2,
                        ((self.position.y - (self.size.y/2)) + (self.margin/2) + ((py.FONT_HEIGHT)*i)) + (self.space*i),
                        self.items[i],
                        self.textColor)
            else:
                skillColor = getSkillColor(self.items[i])
                if skillColor != -1:
                    if self.items[i].cost > player.currMP: #TODO CHANGE player FOR CURR CHARACTER
                        skillColor = py.COLOR_GRAY
                    py.text((self.position.x - (self.size.x/2)) + (self.margin/2) + 2,
                            ((self.position.y - (self.size.y/2)) + (self.margin/2) + ((py.FONT_HEIGHT)*i)) + (self.space*i),
                            f"{self.items[i].name} - {self.items[i].cost}MP",
                            skillColor)
            if i == self.selector:
                py.circ((self.position.x - self.size.x/2) + self.margin/2 - 3, 
                        ((self.position.y - (self.size.y/2)) + (self.margin/2) + ((py.FONT_HEIGHT)*i)) + (self.space*i) + 2,
                        2,
                        py.COLOR_BLACK)  
                
    def UP(self):
        if self.selector > 0:
            self.selector -= 1
    
    def DOWN(self):
        if self.selector < len(self.items)-1:
            self.selector += 1
    
    def SELECT(self) -> int:
        print(self.items[self.selector])
        if player.currMP >= self.items[self.selector].cost:
            if self.items[self.selector].name == "Bufu":
                enemies.addChar(drifter)
            enemieSelctor.skillSelected = self.items[self.selector]
            return 1
        else:
            return 0

class CharPanel(Panel):
    char : CharProfile
    textColor : int
    margin : int
    space : int 

    def __init__(self, x : int, y : int, width : int, panel_color : int, char : CharProfile, margin : int = 8, space : int = 4):
        self.margin = margin
        self.space = space
        self.char = char
        super().__init__(x, y, width+(margin)-1, (3*py.FONT_HEIGHT) + (margin) + (space*(2))-1, panel_color)
    
    def draw(self):
        super().draw()
        py.text((self.position.x - (self.size.x/2)) + (self.margin/2),
                ((self.position.y - (self.size.y/2)) + (self.margin/2) + ((py.FONT_HEIGHT)*0)) + (self.space*0),
                self.char.name,
                py.COLOR_BLACK)
        py.text((self.position.x - (self.size.x/2)) + (self.margin/2),
                ((self.position.y - (self.size.y/2)) + (self.margin/2) + ((py.FONT_HEIGHT)*1)) + (self.space*1),
                f"HP : {self.char.currHP}/{self.char.maxHP}",
                py.COLOR_RED)
        py.text((self.position.x - (self.size.x/2)) + (self.margin/2),
                ((self.position.y - (self.size.y/2)) + (self.margin/2) + ((py.FONT_HEIGHT)*2)) + (self.space*2),
                f"MP : {self.char.currMP}/{self.char.maxMP}",
                py.COLOR_DARK_BLUE)


class EnemiesPanel():
    enemies : list[CharProfile]
    enemiesPanels : list[CharPanel] = []
    selectedEnemie : CharPanel = None
    
    def __init__(self, enemies : list):
        self.enemies = enemies
        for i in range(len(self.enemies)):
            self.enemiesPanels.append(CharPanel((WIDTH/(len(self.enemies)+1))*(i+1),HEIGHT/5,py.FONT_WIDTH*15,py.COLOR_WHITE,self.enemies[i],16,4))

    def addChar(self, enemie : CharProfile):
        self.enemies.append(enemie)
        self.update()

    def update(self):
        self.enemiesPanels = []
        for i in range(len(self.enemies)):
            if self.selectedEnemie == self.enemies[i]:
                self.enemiesPanels.append(CharPanel((WIDTH/(len(self.enemies)+1))*(i+1),HEIGHT/5,py.FONT_WIDTH*15,py.COLOR_GRAY,self.enemies[i],16,4))
            else:
                self.enemiesPanels.append(CharPanel((WIDTH/(len(self.enemies)+1))*(i+1),HEIGHT/5,py.FONT_WIDTH*15,py.COLOR_WHITE,self.enemies[i],16,4))

    def draw(self):
        for enemies in self.enemiesPanels:
            enemies.draw()

class enemieSelector():
    selector : int = 0
    skillSelected : sk.Skill

    def draw(self):
        for i in range(len(enemies.enemies)):
            if i == self.selector:
                enemies.selectedEnemie = enemies.enemies[self.selector]
            '''
            if i == self.selector:
                py.blt((WIDTH/(len(enemies.enemies)+1))*(i+1)-7,5,
                       0,
                       0,0,
                       16,16,1,scale=1.5)
            '''
    def LEFT(self):
        if self.selector != 0:
            self.selector -= 1

    def RIGHT(self):
        if self.selector < len(enemies.enemies)-1:
            self.selector += 1
    
    def SELECT(self) -> int:
        print(enemies.enemies[self.selector])
        enemies.enemies[self.selector].currHP -= 50
        if enemies.enemies[self.selector].currHP <= 0:
            enemies.enemies.remove(enemies.enemies[self.selector])
        enemies.selectedEnemie = None
        player.currMP -= self.skillSelected.cost
        self.selector = 0
        return 0

class CharProfile():
    name : str
    maxHP : int
    currHP : int
    maxMP : int
    currMP : int
    skills : list[sk.Skill] = [sk.attack]
    
    def __init__(self, name : str, HP : int, MP : int):
        self.name = name
        self.maxHP = HP
        self.currHP = HP
        self.maxMP = MP
        self.currMP = MP
    
    def addSkill(self, newSkill : sk.Skill):
        self.skills.append(newSkill)

def getSkillColor(skill : sk.Skill) -> int:
    match skill.type:
        case sk.Type.AUTO:
            return -1
        case sk.Type.PHYS:
            return py.COLOR_ORANGE
        case sk.Type.FIRE:
            return py.COLOR_RED
        case sk.Type.ICE:
            return py.COLOR_LIGHT_BLUE
        case sk.Type.ELEC:
            return py.COLOR_YELLOW
        case sk.Type.FORCE:
            return py.COLOR_GREEN
        case sk.Type.LIGHT:
            return py.COLOR_WHITE
        case sk.Type.DEATH:
            return py.COLOR_PURPLE
        case sk.Type.RECOVERY:
            return py.COLOR_CYAN
        case sk.Type.SUPPORT:
            return py.COLOR_NAVY
        case sk.Type.ALMIGHTY:
            return py.COLOR_PEACH
        
drifter = CharProfile("Drifter", 170, 12)
drifter2 = CharProfile("Drifter", 170, 12)
drifter3 = CharProfile("Drifter", 170, 12)
player = CharProfile("Commando", 110, 12)
player.addSkill(sk.bufu)
player.addSkill(sk.agi)
player.addSkill(sk.zan)
debugPanel = Panel(WIDTH/2,HEIGHT/2,200,200,py.COLOR_WHITE)
skillList = ListPanel(py.FONT_WIDTH*(15),204 - py.FONT_HEIGHT*(len(player.skills)-1),py.FONT_WIDTH*(15),player.skills,py.COLOR_WHITE,py.COLOR_BLACK,16,4)
playerPanel = CharPanel(WIDTH/5*4.35,HEIGHT/7*6,py.FONT_WIDTH*15,py.COLOR_WHITE,player,16,4)
enemies = EnemiesPanel([drifter,drifter2,drifter3])
enemieSelctor = enemieSelector()

