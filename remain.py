import os
import openpyxl

# File paths
excel_file = "aryan 1000.xlsx"   # Your Excel file name
save_dir = "Downloaded_Images"

# Create save directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)

# Load Excel workbook
wb = openpyxl.load_workbook(excel_file)
sheet = wb.active

# Collect all IDs from Excel column A
ids_from_excel = []
row_num = 1
while True:
    id_number = sheet[f"A{row_num}"].value
    if id_number is None:  # Stop when no more IDs
        break
    ids_from_excel.append(str(id_number))
    row_num += 1

# Get all existing folders in save_dir
existing_folders = set(os.listdir(save_dir))

# Track missing folders
missing_folders = []

# Create missing folders only
for id_number in ids_from_excel:
    folder_path = os.path.join(save_dir, id_number)
    if id_number not in existing_folders:  # Only if folder does not exist
        os.makedirs(folder_path, exist_ok=True)
        missing_folders.append(id_number)

# Final report
if missing_folders:
    print(f"📂 Created {len(missing_folders)} missing folders.")
    print("IDs created:", ", ".join(missing_folders))
else:
    print("✅ All folders already exist. Nothing new created.")
