class Type():
    AUTO = 0
    PHYS = 1
    FIRE = 2
    ICE = 3
    ELEC = 4
    FORCE = 5
    LIGHT = 6
    DEATH = 7
    RECOVERY = 8
    SUPPORT = 9
    ALMIGHTY = 10

class Skill():
    name : str
    cost : int
    type : Type

    def __init__(self, name : str, cost : int, type : Type):
        self.name = name
        self.cost = cost
        self.type = type

attack = Skill("Attack", 0, Type.PHYS)
bufu = Skill("Bufu", 3, Type.ICE)
agi = Skill("Agi", 3, Type.FIRE)
zan = Skill("Zan", 3, Type.FORCE)
zio = Skill("Zio", 3, Type.ELEC)
hama = Skill("Hama", 3, Type.LIGHT)
mudo = Skill("Mudo", 3, Type.DEATH)
dia = Skill("Dia", 5, Type.RECOVERY)
tarukaja = Skill("Tarukaja", 10, Type.SUPPORT)
megido = Skill("Megido", 10, Type.ALMIGHTY)