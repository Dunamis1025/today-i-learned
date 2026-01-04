from random import randint

# ==================================================
# 1. Base Units
# ==================================================
# This section defines the most basic unit classes.
# All other units will inherit from these classes.
# ==================================================

class Unit:
    def __init__(self, name, hp, speed):
        """
        __init__ (constructor):
        - Automatically called when a new object is created.
        - Used to initialize the unit's basic attributes.
        """

        # self refers to the current instance (object).
        # We use self to store values that belong to this unit.
        self.name = name      # Unit name
        self.hp = hp          # Health points
        self.speed = speed   # Movement speed

        print("{0} unit has been created.".format(self.name))

    def move(self, location):
        """
        Move the unit toward a specific direction.
        """
        print("{0} : moves toward {1}. [Speed {2}]"
              .format(self.name, location, self.speed))

    def damaged(self, damage):
        """
        Apply damage to the unit.
        If HP becomes 0 or less, the unit is destroyed.
        """
        print("{0} : has taken {1} damage."
              .format(self.name, damage))
        self.hp -= damage
        print("{0} : current HP {1}"
              .format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : has been destroyed."
                  .format(self.name))


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        """
        AttackUnit is a Unit that can attack enemies.
        """

        # super() calls the parent class (Unit).
        # This reuses Unit's __init__ method.
        super().__init__(name, hp, speed)

        # Damage value for attack units
        self.damage = damage

    def attack(self, location):
        """
        Attack enemies toward a specific direction.
        """
        print("{0} : attacks toward {1}. [Damage {2}]"
              .format(self.name, location, self.damage))
