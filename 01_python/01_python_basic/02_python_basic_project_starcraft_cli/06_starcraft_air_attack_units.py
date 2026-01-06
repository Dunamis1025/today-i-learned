from random import randint

# ==================================================
# 1. Base Units
# ==================================================
# This section defines the most fundamental unit classes.
# All other units (Marine, Tank, Wraith, etc.)
# will inherit from these base classes.
#
# This part forms the core structure of the entire project.
# ==================================================

class Unit:
    def __init__(self, name, hp, speed):
        """
        __init__ (constructor):
        - Automatically called when a new object (instance) is created
        - Initializes the unit's core attributes
        """

        # self refers to the current instance being created
        # Attributes stored in self belong to each individual unit
        self.name = name      # Unit name
        self.hp = hp          # Health points
        self.speed = speed   # Movement speed

        print("{0} unit has been created.".format(self.name))

    def move(self, location):
        """
        Move the unit toward a specific direction.
        This is a CLI simulation, not real in-game movement.
        """
        print("{0} : Moving toward {1}. [Speed {2}]"
              .format(self.name, location, self.speed))

    def damaged(self, damage):
        """
        Apply damage to the unit.
        If HP becomes 0 or less, the unit is destroyed.
        """
        print("{0} : Took {1} damage."
              .format(self.name, damage))

        self.hp -= damage
        print("{0} : Current HP {1}"
              .format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : Destroyed."
                  .format(self.name))


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        """
        AttackUnit:
        - A unit that can attack enemies
        - Inherits movement and HP logic from Unit
        """

        # super() calls the parent class (Unit) constructor
        # This avoids duplicating initialization logic
        super().__init__(name, hp, speed)

        # Attribute specific to attack-capable units
        self.damage = damage

    def attack(self, location):
        """
        Attack enemies toward a specific direction.
        """
        print("{0} : Attacking toward {1}. [Damage {2}]"
              .format(self.name, location, self.damage))


# ==================================================
# 2. Ground Attack Units
# ==================================================
# Units that move and attack on the ground
# ==================================================

class Marine(AttackUnit):
    def __init__(self):
        # Marine has fixed base stats
        super().__init__("Marine", 40, 1, 5)

    def stimpack(self):
        """
        Stimpack ability:
        - Conceptually boosts performance
        - Costs 10 HP to activate
        """
        if self.hp > 10:
            self.hp -= 10
            print("{0} : Using Stimpack. (HP -10)"
                  .format(self.name))
        else:
            print("{0} : Not enough HP to use Stimpack."
                  .format(self.name))


class Tank(AttackUnit):
    # Class variable:
    # Shared across all Tank instances
    siege_developed = False

    def __init__(self):
        super().__init__("Tank", 150, 1, 35)
        self.siege_mode = False

    def set_siege_mode(self):
        """
        Siege Mode:
        - Requires siege research
        - Doubles attack damage
        - Uses toggle (ON / OFF) logic
        """
        if not Tank.siege_developed:
            return

        if not self.siege_mode:
            self.damage *= 2
            self.siege_mode = True
            print("{0} : Entering Siege Mode."
                  .format(self.name))
        else:
            self.damage //= 2
            self.siege_mode = False
            print("{0} : Exiting Siege Mode."
                  .format(self.name))


# ==================================================
# 3. Air Attack Units
# ==================================================
# Units that can fly and attack.
#
# Key concepts introduced here:
# - Multiple inheritance
# - Method overriding
# - Separating ground movement and air movement
# ==================================================

class Flyable:
    def __init__(self, flying_speed):
        # flying_speed is stored as an instance variable
        # because each flying unit may have different speed
        self.flying_speed = flying_speed

    def fly(self, name, location):
        """
        Move the unit by flying.
        """
        print("{0} : Flying toward {1}. [Speed {2}]"
              .format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        """
        A unit that can both fly and attack.
        Demonstrates multiple inheritance.
        """

        # Ground speed is set to 0 for flying units
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        """
        Method override:
        Flying units use fly() instead of ground movement.
        """
        self.fly(self.name, location)


class Wraith(FlyableAttackUnit):
    def __init__(self):
        # super() calls the parent class constructor
        super().__init__("Wraith", 80, 20, 5)
        self.cloaked = False

    def cloaking(self):
        """
        Toggle cloaking mode ON / OFF.
        Toggle means switching between two states.
        """
        if self.cloaked:
            print("{0} : Cloaking deactivated."
                  .format(self.name))
            self.cloaked = False
        else:
            print("{0} : Cloaking activated."
                  .format(self.name))
            self.cloaked = True
