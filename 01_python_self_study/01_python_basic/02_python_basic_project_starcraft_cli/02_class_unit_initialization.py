# ===============================
# StarCraft CLI - Unit Class Initialization
# ===============================
# Goal:
# - Create a Unit class
# - Initialize multiple units (Marine, Tank)
# - Display unit stats using __init__()

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

        print("{0} unit has been created.".format(self.name))
        print("HP: {0}, Damage: {1}\n".format(self.hp, self.damage))


# -------------------------------
# Unit creation
# -------------------------------
marine1 = Unit("Marine", 40, 5)
marine2 = Unit("Marine", 40, 5)
tank = Unit("Tank", 150, 35)
