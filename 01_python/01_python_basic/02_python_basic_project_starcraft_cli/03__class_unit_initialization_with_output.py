# ==================================================
# StarCraft Unit Class Example
# - Class constructor (__init__)
# - Meaning of self
# - Instance-specific attributes
# ==================================================

class Unit:
    def __init__(self, name, hp, damage):
        """
        __init__ (constructor):
        - Automatically called when a new object is created from the class
        - Used to initialize the unit with required attributes
        """

        # self refers to the current instance being created
        # Each object created from the same class can have different values
        self.name = name      # Unit name
        self.hp = hp          # Health points
        self.damage = damage  # Attack damage

        # Display unit creation information
        print("{0} unit has been created.".format(self.name))
        print("HP {0}, Damage {1}".format(self.hp, self.damage))


# --------------------------------------------------
# Unit creation examples (commented out)
# --------------------------------------------------
# marine1 = Unit("Marine", 40, 5)
# marine2 = Unit("Marine", 40, 5)
# tank = Unit("Tank", 150, 35)


# --------------------------------------------------
# Wraith unit example
# --------------------------------------------------
# Wraith: air unit (can fly)
wraith1 = Unit("Wraith", 80, 5)

# Access instance attributes using dot notation
print("Unit Name: {0}, Damage: {1}".format(wraith1.name, wraith1.damage))


# --------------------------------------------------
# Mind Control example
# --------------------------------------------------
# Mind Control: stealing an enemy unit and making it your own
wraith2 = Unit("Captured Wraith", 80, 5)

# Attributes not defined in the class
# can be dynamically added to a specific instance
# (In this case, only wraith2 has the 'cloaking' attribute)
wraith2.cloaking = True

# Check cloaking status
if wraith2.cloaking:
    print("{0} is currently cloaked.".format(wraith2.name))


# ==================================================
# Program Output
# ==================================================
# Wraith unit has been created.
# HP 80, Damage 5
# Unit Name: Wraith, Damage: 5
# Captured Wraith unit has been created.
# HP 80, Damage 5
# Captured Wraith is currently cloaked.
