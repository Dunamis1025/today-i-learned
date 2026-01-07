# StarCraft CLI OOP Project

This project is a **command-line (CLI) simulation inspired by StarCraft**, created to practice and demonstrate core **Object-Oriented Programming (OOP)** concepts in Python.

Rather than focusing on graphics or real-time gameplay, this project emphasizes **clean class design, inheritance structure, and game-like logic flow** using simple console output.

The project was built incrementally, with each step adding new concepts and functionality, and finally integrated into a complete game simulation.

---

## 🎯 Project Goals

- Understand and apply **Object-Oriented Programming** fundamentals
- Practice designing a scalable class hierarchy
- Learn how different unit types can share and override behavior
- Simulate a simple game flow using Python logic
- Build a readable, well-structured CLI project for learning and review

---

## 🧠 Key Concepts Covered

- **Classes and Objects**
- **Constructors (`__init__`)**
- **Inheritance**
- **Polymorphism**
- **Multiple Inheritance**
- **Method Overriding**
- **Class Variables vs Instance Variables**
- **`isinstance()` for type-based behavior control**
- **Simple game loop and state flow**

---

## 🧩 Project Structure

Each file represents a learning step and builds upon the previous one:

- Base unit creation and initialization
- Attack-capable units
- Ground units (Marine, Tank) with special abilities
- Air units (Wraith) using multiple inheritance
- Game control functions (start / end)
- Full game simulation integrating all units and mechanics

This step-by-step approach makes it easy to review specific OOP concepts in isolation or understand how they work together as a system.

---

## 🎮 Game Flow Overview

1. Game starts
2. Units are created
3. All units move (ground units move, air units fly)
4. Special abilities are activated based on unit type
5. All units attack
6. Units take random damage
7. Game ends

Each phase is clearly printed to the console to visualize the flow.

---

## 📌 Result Output

Below is the output produced when running the final simulation script:



Result
[NOTICE] A new game has started.

Marine unit has been created.
Marine unit has been created.
Marine unit has been created.
Tank unit has been created.
Tank unit has been created.
Wraith unit has been created.

[ALL UNITS MOVING]
Marine : Moving toward 1 o'clock. [Speed 1]
Marine : Moving toward 1 o'clock. [Speed 1]
Marine : Moving toward 1 o'clock. [Speed 1]
Tank : Moving toward 1 o'clock. [Speed 1]
Tank : Moving toward 1 o'clock. [Speed 1]
Wraith : Flying toward 1 o'clock. [Speed 5]

[NOTICE] Tank siege mode research completed.

[SPECIAL ABILITIES]
Marine : Using Stimpack. (HP -10)
Marine : Using Stimpack. (HP -10)
Marine : Using Stimpack. (HP -10)
Tank : Entering Siege Mode.
Tank : Entering Siege Mode.
Wraith : Cloaking activated.

[ALL UNITS ATTACKING]
Marine : Attacking toward 1 o'clock. [Damage 5]
Marine : Attacking toward 1 o'clock. [Damage 5]
Marine : Attacking toward 1 o'clock. [Damage 5]
Tank : Attacking toward 1 o'clock. [Damage 70]
Tank : Attacking toward 1 o'clock. [Damage 70]
Wraith : Attacking toward 1 o'clock. [Damage 20]

[DAMAGE PHASE]
Marine : Took 12 damage.
Marine : Current HP 18
...
Tank : Took 15 damage.
Tank : Current HP 135
...

Player : gg
[NOTICE] The game has ended.


---

## ✅ Summary

This project serves as a **hands-on OOP learning exercise** and a reference implementation for building structured, object-oriented Python programs.

It focuses on clarity, readability, and conceptual correctness rather than performance or complexity, making it ideal for beginners revisiting OOP fundamentals or developers wanting a clean example of class-based design.
