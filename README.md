# Image-Scraper
Image scraper using python
Got it 👍 — you want a proper **README file text** that explains everything step by step about how to set up and run your Python script.  
Here’s a ready-to-use `README.md` draft for your project:

***

# 📸 College Campus Image Downloader

This project is a **semi-automatic image downloader** that helps you collect campus photos for a list of colleges stored in an Excel file.  

The script will:
- Open Google Image Search for each college (with "campus photos" keyword).
- Wait for you to copy an image URL (right-click → "Copy image address").
- Automatically download and save the image.
- Keep track of progress (`last_done.txt`) so you can resume anytime.

***

## 🚀 Features
- Works directly from a list in Excel (`aryan 1000.xlsx`).
- Creates a separate folder for each college (based on ID).
- Downloads up to **3 images per college**.
- Allows **skip, wait, or exit** choices interactively.
- Automatically saves progress so you can stop and resume later.

***

## 📂 Project Structure

```
project/
│── aryan 1000.xlsx        # Excel file with IDs and college names
│── script.py              # Your Python script (this code)
│── Downloaded_Images/     # Folder where images are saved
│── last_done.txt          # Progress file
│── README.md              # (This file)
```

***

## 📋 Requirements

### Python Version
- Python **3.8+**  

### Install Dependencies
Run the following command in your terminal or command prompt:

```bash
pip install requests openpyxl pillow pyperclip
```

*(Windows only: `msvcrt` is included by default, no need to install.)*

***

## 📝 Preparing the Excel File

Your Excel (`aryan 1000.xlsx`) should look like this:

| ID (A) | ... | College Name (C) | College Name (D) |
|--------|-----|------------------|------------------|
| 1      | ... | Delhi University | North Campus     |
| 2      | ... | IIT Bombay       | -                |
| 3      | ... | NIT Trichy       | -                |

The script will combine `Column C + Column D` into the search query.

***

## ▶️ Running the Script

Run the program with:

```bash
python script.py
```

***

## 🔧 How It Works (Step by Step)

1. The script starts and checks `last_done.txt` to know where you left off.
2. For each college:
   - A **Google Image Search** opens automatically in your browser.
   - Right-click on a good image → **Copy Image Address**.
   - The script detects the copied URL and downloads the image.
3. Each college gets a dedicated folder under `Downloaded_Images/[ID]/`.
4. The script saves up to **3 images per college**.
5. If 60 seconds pass with no URL copied:
   - You’ll be prompted to skip, keep waiting, or exit.
6. At any moment:
   - Press **S** → Skip image  
   - Press **E** → Exit program  
   - Press **Enter** when prompted → Move to next college
7. Progress is always saved (`last_done.txt`).

***

## ⌨️ Controls During Execution

- **Copy URL** → Downloads image
- **S** → Skip current image immediately
- **E** → Exit program safely
- **Enter** → Skip to next college
- **wait** → Continue waiting for a URL

***

## 💾 Saved Files

- **Images:**  
  Stored under `Downloaded_Images/[ID]/1.jpg`, `2.jpg`, `3.jpg`.

- **Progress:**  
  Stored in `last_done.txt` (holds the last completed row number).  

This means you can stop the script anytime and restart later—it will pick up from where you left.

***

## ⚠️ Notes & Tips
- Use **Chrome or Firefox** for copying "Image Address".
- Some image URLs may not work (e.g., Google cached thumbnails). If download fails, just copy a different image.
- Recommended to use with a **stable internet connection**.
- You must manually select **good quality campus photos**—the script doesn’t choose automatically.

***

## ✅ Example Run

```
🏫 Processing ID: 12 | College: IIT Bombay
📊 Progress: Row 12 | Need 2 more images

📸 Getting image 1/3 for 12...
📋 Waiting for URL in clipboard... (Copy an image URL from browser)
✅ URL detected: https://example.com/iitb-campus.jpg...
⬇️ Downloading image...
📏 Image dimensions: 1920x1080 (2.07MP)
✅ Saved image: 1.jpg
```

***

This way, you and anyone using it will know **exactly how to set up and run it**.

***

👉 Do you want me to also create a **short "Quick Start" section** (3 steps only) at the top of the README for easy use?

This tool opens Google Images in your browser and downloads URLs you manually select. Respect copyright and usage terms of any images you save.
