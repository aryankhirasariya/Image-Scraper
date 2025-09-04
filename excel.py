import openpyxl

# File path to your Excel file
excel_file = "aryan 1000.xlsx"

# Load workbook and select active sheet
wb = openpyxl.load_workbook(excel_file)
sheet = wb.active

# Keep a set of college names we have already seen
seen = set()

# Loop through all rows and clear duplicates (C and D columns)
for row in range(2, sheet.max_row + 1):
    name_c = sheet[f"C{row}"].value or ""
    name_d = sheet[f"D{row}"].value or ""
    full_name = f"{name_c} {name_d}".strip()

    if full_name:                    # If name is not empty
        if full_name in seen:        # Already seen => clear
            sheet[f"C{row}"].value = ""
            sheet[f"D{row}"].value = ""
        else:
            seen.add(full_name)      # First occurrence => keep

# Save the workbook
wb.save(excel_file)

print("✅ Repeated college names have been cleared (only first occurrence kept).")
