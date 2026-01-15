📦 Python Package Basics – Clean Summary (English)
1️⃣ What is a Package?

A package in Python is
👉 a way to group multiple Python files (.py) into a single folder and manage them together.

As projects grow, putting everything into one file becomes hard to manage.

By organizing related code into folders:

The structure becomes clearer

Code is easier to reuse

Other people can understand the project more easily

📌 In short, a package is a folder used to organize related Python code.

2️⃣ Folder Structure Used in This Example
project/
│
├─ travel/                 ← Package folder
│   ├─ __init__.py         ← Marks this folder as a Python package
│   ├─ thailand.py         ← Thailand travel module
│   └─ vietnam.py          ← Vietnam travel module
│
└─ practice.py             ← Script that uses the package


📌 __init__.py

Can be empty

Its role is to tell Python:
“This folder is a Python package.”

3️⃣ Role of Each File
📄 thailand.py
class ThailandPackage:
    def detail(self):
        print("[Thailand Package 3N 5D] Bangkok, Pattaya Trip (Night Market Tour) $500")


✔ Defines a Thailand travel product as a class
✔ The detail() method prints package information

📄 vietnam.py
class VietnamPackage:
    def detail(self):
        print("[Vietnam Package 3N 5D] Da Nang Family Trip $600")


✔ Defines a Vietnam travel product
✔ Same structure as the Thailand package

👉 This structure makes it easy to add more country packages later.

4️⃣ Using the Package in practice.py
✅ Method 1: Import the entire module
import travel.thailand

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()


Meaning:

Imports the entire travel.thailand module

The full path must be used to access the class

📌 Pros: Clear where the class comes from
📌 Cons: Slightly longer code

✅ Method 2: Import a specific class
from travel.thailand import ThailandPackage

trip_to = ThailandPackage()
trip_to.detail()


Meaning:

Imports only the ThailandPackage class

Can use the class name directly

📌 Pros: Short and clean
📌 Cons: Source can be unclear in larger projects

✅ Method 3: Import another module (vietnam)
from travel import vietnam

trip_to = vietnam.VietnamPackage()
trip_to.detail()


Result:

[Vietnam Package 3N 5D] Da Nang Family Trip $600

5️⃣ Key Concepts Learned from This Example

✅ 1. A package is “a folder + __init__.py”
Python recognizes the folder as a package because of this file.

✅ 2. A module is a .py file
thailand.py and vietnam.py are modules inside the package.

✅ 3. There are multiple ways to import

import package.module

from package import module

from package.module import Class

👉 Choose the method based on readability and project size.

✅ 4. Why packages are useful

Better organization

Easier expansion

Improved readability

Easier maintenance

6️⃣ One-Line Summary (for GitHub)

A Python package is a folder that groups related Python files together,
allowing code to be organized, reused, and imported in a structured way.
