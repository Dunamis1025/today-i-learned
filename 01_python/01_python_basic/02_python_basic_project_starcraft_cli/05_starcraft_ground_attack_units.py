from random import randint

# ==================================================
# 1. Base Units
# ==================================================
# This section defines the most fundamental unit classes.
# All other units (Marine, Tank, etc.) will inherit from these classes.
# These classes form the core structure of the entire project.
# ==================================================

class Unit:
    def __init__(self, name, hp, speed):
        """
        __init__ (constructor):
        - Automatically called when a new object (instance) is created.
        - Initializes the unit's basic attributes.
        """

        # self refers to the current instance being created.
        # Attributes stored in self belong to this specific object.
        self.name = name      # Unit name
        self.hp = hp          # Health points
        self.speed = speed    # Movement speed

        print("{0} unit has been created.".format(self.name))

    def move(self, location):
        """
        Move the unit toward a specific direction.
        This is a CLI simulation, not actual in-game movement.
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

        # Reduce HP by the damage amount
        self.hp -= damage

        print("{0} : Current HP {1}"
              .format(self.name, self.hp))

        # Destroy unit if HP is 0 or below
        if self.hp <= 0:
            print("{0} : Destroyed."
                  .format(self.name))


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        """
        AttackUnit:
        - An extended unit that can attack enemies.
        - Inherits movement and HP logic from Unit.
        """

        # super() explanation:
        # Calls the parent class (Unit) constructor.
        # This avoids duplicating initialization code for name, hp, and speed.
        super().__init__(name, hp, speed)

        # Additional attribute specific to attack units
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
# Units that attack on the ground (Marine, Tank, etc.)
# ==================================================

class Marine(AttackUnit):
    def __init__(self):
        # Marine is a ground attack unit.
        # Fixed base stats are defined here.
        super().__init__("Marine", 40, 1, 5)

    def stimpack(self):
        """
        Stimpack ability:
        - Temporarily boosts performance (conceptual).
        - Costs 10 HP to use.
        """

        # Prevent using stimpack if HP is too low.
        if self.hp > 10:
            self.hp -= 10
            print("{0} : Using Stimpack. (HP -10)"
                  .format(self.name))
        else:
            print("{0} : Not enough HP to use Stimpack."
                  .format(self.name))


class Tank(AttackUnit):
    # Class variable:
    # Shared across ALL Tank instances.
    # Research completion should affect every tank, not just one.
    siege_developed = False

    def __init__(self):
        super().__init__("Tank", 150, 1, 35)

        # Instance variable:
        # Each tank must track its own siege mode state independently.
        self.siege_mode = False

    def set_siege_mode(self):
        """
        Siege Mode:
        - Requires siege research to be completed.
        - Doubles attack damage when enabled.
        - Acts as a toggle (ON / OFF).
        """

        # If siege research is not completed, do nothing.
        if not Tank.siege_developed:
            return

        # Toggle logic explanation:
        # - If siege_mode is False (currently OFF),
        #   switch it ON and increase damage.
        # - If siege_mode is True (currently ON),
        #   switch it OFF and restore original damage.

        # Why "if not self.siege_mode"?
        # This condition checks whether the tank is NOT in siege mode.
        # It clearly represents the transition from OFF -> ON.
        if not self.siege_mode:
            # Entering siege mode:
            # Damage is increased because siege mode is more powerful.
            self.damage *= 2

            # Update state to ON
            self.siege_mode = True

            print("{0} : Entering Siege Mode."
                  .format(self.name))
        else:
            # Exiting siege mode:
            # Damage must return to its original value.
            # Integer division (//=) is used to keep damage as an integer.
            self.damage //= 2

            # Update state to OFF
            self.siege_mode = False

            print("{0} : Exiting Siege Mode."
                  .format(self.name))
