# ===============================
# StarCraft CLI - Basic Unit Initialization
# ===============================
# Goal:
# - Create basic units (Marine, Tank)
# - Display unit stats
# - Simulate a simple attack in the terminal (CLI)

# -------------------------------
# Marine: Attack unit (soldier)
# -------------------------------
marine_name = "Marine"   # unit name
marine_hp = 40           # unit HP
marine_damage = 5        # unit damage

print("{0} unit has been created.".format(marine_name))
print("HP: {0}, Damage: {1}\n".format(marine_hp, marine_damage))

# -------------------------------
# Tank: Attack unit (vehicle)
# - Can fire a cannon (normal mode / siege mode later)
# -------------------------------
tank_name = "Tank"
tank_hp = 150
tank_damage = 35

print("{0} unit has been created.".format(tank_name))
print("HP: {0}, Damage: {1}\n".format(tank_hp, tank_damage))


def attack(unit_name, direction, unit_damage):
    """
    unit_name   : name of the unit
    direction   : attack direction
    unit_damage : damage value
    """
    print("{0} attacks the enemy towards {1}. [Damage: {2}]".format(
        unit_name, direction, unit_damage
    ))


# -------------------------------
# Attack simulation
# -------------------------------
attack(marine_name, "1 o'clock", marine_damage)
attack(tank_name, "1 o'clock", tank_damage)

"""
# Output (Expected Result)

Marine unit has been created.
HP: 40, Damage: 5

Tank unit has been created.
HP: 150, Damage: 35

Marine attacks the enemy towards 1 o'clock. [Damage: 5]
Tank attacks the enemy towards 1 o'clock. [Damage: 35]
"""
