"""
📌 Inserting Rows and Columns in an Existing Excel File (openpyxl)

This file demonstrates how to:
- Insert new rows at a specific position
- Insert new columns at a specific position
- Understand how existing data is shifted
- Save the result as a new file to protect the original data

❗ Purpose
- Focus on understanding structural changes in Excel
- Learn how insert_rows() and insert_cols() affect existing data
- Keep this file as a reference for future automation tasks
"""

# ==================================================
# 1️⃣ Load an existing Excel file
# ==================================================
from openpyxl import load_workbook

# Load the existing Excel file
wb = load_workbook("sample.xlsx")

# Get the active worksheet
ws = wb.active


# ==================================================
# 2️⃣ Insert rows
# ==================================================
"""
ws.insert_rows(idx, amount=1)

- Inserts empty row(s) at the given row index
- Existing rows at and below the index are shifted downward
- No data is deleted; only positions change

Examples:
"""

# ws.insert_rows(8)        # Insert 1 empty row at row 8
# ws.insert_rows(8, 5)     # Insert 5 empty rows starting at row 8
# wb.save("sample_insert_rows.xlsx")


# ==================================================
# 3️⃣ Insert columns
# ==================================================
"""
ws.insert_cols(idx, amount=1)

- Inserts empty column(s) at the given column index
- Existing columns at and to the right are shifted to the right

Column index reference:
1 = A, 2 = B, 3 = C, ...
"""

# ws.insert_cols(2)        # Insert 1 empty column at column B
ws.insert_cols(2, 3)       # Insert 3 empty columns starting at column B


# ==================================================
# 4️⃣ Save the modified workbook
# ==================================================
"""
Important:
- Do not overwrite the original file
- Always save structural changes as a new file
"""
wb.save("sample_insert_cols.xlsx")
