"""
📌 Inserting an Image into an Excel File (openpyxl)

This script demonstrates how to use the openpyxl library to:
- Create a new Excel workbook
- Insert an image (PNG) into a specific cell
- Save the Excel file with the image included

📂 Notes
- This Python file and the image file (image.png) must be in the same directory.
- The image file name and extension must match exactly.
"""

# ==================================================
# 1️⃣ Import required libraries
# ==================================================
from openpyxl import Workbook
from openpyxl.drawing.image import Image


# ==================================================
# 2️⃣ Create a new Excel workbook
# ==================================================
wb = Workbook()        # Create a new Excel workbook
ws = wb.active        # Select the active worksheet


# ==================================================
# 3️⃣ Load the image file
# ==================================================
# Load image.png from the same directory as this script
img = Image("image.png")


# ==================================================
# 4️⃣ Insert the image into the worksheet
# ==================================================
# Insert the image at cell C3
ws.add_image(img, "C3")


# ==================================================
# 5️⃣ Save the Excel file
# ==================================================
# Save the Excel file with the inserted image
wb.save("sample_image.xlsx")
