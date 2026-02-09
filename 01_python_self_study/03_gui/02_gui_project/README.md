Image Merge GUI Project (Tkinter)

This folder contains a complete Tkinter-based GUI project that merges multiple images into a single output image.

The project is built step by step, applying and extending concepts learned in 01_gui_basic, and gradually evolving into a stable, user-friendly GUI application.

🎯 Project Goal

The goal of this project is to:

Apply Tkinter basics in a real, functional application

Design a user-friendly GUI workflow

Handle user input safely and predictably

Practice refactoring and incremental feature development

Learn how small GUI concepts connect into a full project

🧩 Project Overview

This application allows the user to:

Select multiple image files

Choose an output destination folder

Configure merge options:

Output width

Spacing between images

Output image format

Track progress visually

Handle invalid input and runtime errors safely

The final output is a single merged image saved to the selected directory.

🛠 Features Implemented
📁 File Handling

Multi-file image selection

Listbox-based file management

Destination folder selection

⚙️ Merge Options

Width

Keep original width or resize while maintaining aspect ratio

Spacing

None / Small / Medium / Large

Format

PNG / JPG / BMP

📊 Progress Tracking

Real-time progress bar updates during merge

Visual feedback for long-running operations

🚨 Exception Handling

Prevents crashes on invalid destination paths

Displays clear error messages using messagebox

Improves overall application stability

🧱 Development Flow

This project was developed incrementally:

Basic GUI layout

File selection and list management

Image merging logic

Progress bar integration

Option handling (width, spacing, format)

Refactoring for readability and safety

Exception handling for real user input scenarios

Each step is preserved as a separate file to clearly show the learning and evolution process.

🖼 Result Screenshots

The folder includes result screenshots that demonstrate:

Successful image merging

Correct application of options

Working progress bar behavior

Completed output notifications

These screenshots serve as both visual verification and documentation.

🔗 Relationship to Other Folders

01_gui_basic
→ Focuses on isolated Tkinter concepts and widgets

02_gui_project
→ Combines those concepts into a complete GUI application

Together, they represent a full learning path from basics to application.

📌 Notes

All code is written for learning purposes

The project structure reflects real-world GUI development patterns

This folder demonstrates how to move from examples to an actual usable tool

🚀 Next Steps

Possible future improvements:

Drag-and-drop file support

Horizontal merge option

Output file name customization

Image preview inside the GUI
