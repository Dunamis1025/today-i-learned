"""
📌 RPA Basics - Excel Automation (openpyxl)
01) Create a new Excel file

This script is a starter example for Excel automation using Python.
It shows the minimum steps needed to create an .xlsx file safely.

What you'll learn in this file:
1) Create a Workbook (an Excel file in memory)
2) Get the active Worksheet (the default sheet that comes with a new workbook)
3) Rename the worksheet (so the file is easier to understand later)
4) Save the workbook as an .xlsx file on disk
5) Close the workbook to release resources properly

Output:
- A file named "sample.xlsx" will be created in the same folder as this script.
"""

from openpyxl import Workbook

# 1) Create a new workbook object.
#    Think of this as creating a brand-new Excel file in memory (not saved yet).
wb = Workbook()

# 2) Get the active worksheet.
#    A new workbook starts with one default sheet, and "active" points to it.
ws = wb.active

# 3) Rename the worksheet.
#    This helps you recognize the sheet later instead of leaving it as "Sheet".
ws.title = "NadoSheet"

# 4) Save the workbook to an actual Excel file on your computer.
#    The file will be created in the current working directory.
#    Tip: If you're not sure where it saves, print the current path:
#    import os; print(os.getcwd())
wb.save("sample.xlsx")

# 5) Close the workbook.
#    Good practice: closes file handles and frees resources.
wb.close()
