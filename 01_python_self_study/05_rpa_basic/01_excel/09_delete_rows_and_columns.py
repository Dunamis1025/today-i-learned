"""
📌 Deleting Rows and Columns in an Existing Excel File (openpyxl)

This file demonstrates how to:
- Delete specific rows from an Excel worksheet
- Delete specific columns from an Excel worksheet
- Understand how remaining data is shifted after deletion
- Save the result as a new file to protect the original data

❗ Purpose
- Learn how to safely remove rows and columns
- Understand irreversible structural changes
- Keep this as a reference for future Excel automation
"""

# ==================================================
# 1️⃣ Load an existing Excel file
# ==================================================
from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")
ws = wb.active


# ==================================================
# 2️⃣ Delete rows
# ==================================================
"""
ws.delete_rows(idx, amount=1)

- Deletes row(s) starting at the given index
- Rows below the deleted area shift upward
"""

# ws.delete_rows(8)        # Delete 1 row at row 8
# ws.delete_rows(8, 3)     # Delete 3 rows starting at row 8
# wb.save("sample_delete_row.xlsx")


# ==================================================
# 3️⃣ Delete columns
# ==================================================
"""
ws.delete_cols(idx, amount=1)

- Deletes column(s) starting at the given index
- Columns to the right shift left

Column index reference:
1 = A, 2 = B, 3 = C, ...
"""

# ws.delete_cols(2)        # Delete column B
ws.delete_cols(2, 2)       # Delete columns B and C


# ==================================================
# 4️⃣ Save the modified workbook
# ==================================================
wb.save("sample_delete_col.xlsx")
