# Image-Scraper
Image scraper using python
Campus Image Downloader

This Python script helps you open Google Image Search for each college in an Excel list, copy image URLs from the browser, and automatically download & save those images into organized folders. It remembers your progress so you can stop and continue anytime.
#################
✨ Features

Reads college IDs and names from an Excel sheet

Opens Google Image Search automatically (with “campus photos” keyword)

Waits for you to copy an image address → auto-detects & downloads

Stores images per college in a separate folder

Saves progress in a text file (last_done.txt) so you can resume later

Skip or exit at any time
###################
📦 Requirements

Python 3.8+

A desktop OS (Windows is assumed for the clipboard/wait code)

Installed Python packages:
pip install openpyxl pillow requests pyperclip

⚠️ The script uses msvcrt (Windows-only) for non-blocking key detection. On Linux/Mac you’d need minor changes.
###################
project/
│
├─ yourexclefile.xlsx        # Your Excel file (ID in column A, college names in C & D)
├─ campus_downloader.py   # This script
├─ last_done.txt          # Created automatically to store progress
└─ Downloaded_Images/     # Created automatically; contains per-ID folders

####################

🔧 Excel File Format

The script expects:

Column A → Unique ID for each college

Column C & Column D → College name (any one or both)

Only rows with a value in Column A are processed.

🚀 How to Run

Place the script, your Excel file (aryan 1000.xlsx) in the same directory.

Open a terminal (Command Prompt / PowerShell) in that directory.

Run:  python campus_downloader.py

The script will:

Open Google Images with "<college name> campus photos"

Prompt you to copy an image URL (Right-click → “Copy image address”).

The script detects the URL and downloads it.

Each college folder gets up to 3 images.

Follow on-screen keys:

Press “s” → Skip current image

Press “e” → Exit immediately

At other prompts:

Press Enter to continue

Type wait to keep waiting for URLs

Type exit to quit

💾 Resuming Work

Progress is saved in last_done.txt.

Restart the script later; it will resume at the next row automatically.

📝 Notes

Script defaults to JPEG format for saving.

Google’s image results can change; you still choose which URL to copy.

For non-Windows OS, replace msvcrt logic with a suitable alternative.

⚖️ Disclaimer

This tool opens Google Images in your browser and downloads URLs you manually select. Respect copyright and usage terms of any images you save.
