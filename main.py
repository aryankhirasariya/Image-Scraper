import os
import requests
import openpyxl
import webbrowser
from PIL import Image
from io import BytesIO
import pyperclip
import time
import urllib.parse

# File paths
excel_file = "aryan 1000.xlsx"   # Your Excel file name
save_dir = "Downloaded_Images"
progress_file = "last_done.txt"

# Create save directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)

# Load Excel workbook
wb = openpyxl.load_workbook(excel_file)
sheet = wb.active

# Read last done row
if os.path.exists(progress_file):
    with open(progress_file, "r") as f:
        last_done = f.read().strip()
        last_done = int(last_done) if last_done.isdigit() else 1
else:
    last_done = 1

def google_search_large_images(college_name):
    """Open Google search with advanced filters for large images (2MP+) and campus keyword"""
    # Add "campus" to the search query
    search_term = f"{college_name} campus photos"
    # URL encode the search term
    encoded_name = urllib.parse.quote(search_term)
    
    # Google advanced search parameters:
    # tbm=isch: image search
    # tbs=isz:lt,islt:2mp: images larger than 2 megapixels
    search_url = f"https://www.google.com/search?tbm=isch&q={encoded_name}&tbs=isz:lt,islt:2mp"
    
    print(f"🔍 Opening Google search for: {search_term} (Images larger than 2MP)")
    webbrowser.open(search_url)

def wait_for_clipboard_url(timeout=30):
    """Wait for a valid URL to appear in clipboard"""
    print("📋 Waiting for URL in clipboard... (Copy an image URL from browser)")
    print("   💡 Tip: Right-click on image → 'Copy image address'")
    print("   ⏭️  Press 's' + Enter to skip this image")
    print("   🚪 Press 'e' + Enter to exit the program")
    
    start_time = time.time()
    last_clipboard = pyperclip.paste()
    
    # Windows-compatible keyboard input checking
    import msvcrt
    
    while time.time() - start_time < timeout:
        # Check for keyboard input (Windows compatible)
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 's':
                print("\n⏭️ Skipping this image...")
                # Clear any remaining input
                while msvcrt.kbhit():
                    msvcrt.getch()
                return 'SKIP'
            elif key == 'e':
                print("\n🚪 Exiting program...")
                # Clear any remaining input
                while msvcrt.kbhit():
                    msvcrt.getch()
                exit(0)
        
        current_clipboard = pyperclip.paste().strip()
        
        # Check if clipboard content changed and is a valid URL
        if (current_clipboard != last_clipboard and 
            current_clipboard and 
            current_clipboard.lower().startswith(('http://', 'https://'))):
            
            print(f"✅ URL detected: {current_clipboard[:60]}...")
            pyperclip.copy("")  # Clear clipboard
            return current_clipboard
        
        time.sleep(0.1)  # Check every 100ms for better responsiveness
        
    return None

def download_image(url, save_path):
    """Download image without size restrictions"""
    try:
        print(f"⬇️ Downloading image...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        
        # Display image dimensions
        width, height = img.size
        megapixels = (width * height) / 1000000
        print(f"📏 Image dimensions: {width}x{height} ({megapixels:.2f}MP)")
        
        # Save the image
        img.save(save_path, "JPEG", quality=90)
        print(f"✅ Saved image: {os.path.basename(save_path)}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error processing image: {e}")
        return False

def get_user_choice():
    """Get user choice for skipping or continuing"""
    print("\n" + "="*50)
    print("🎯 Choose an option:")
    print("   [Enter] - Skip to next college")
    print("   [wait]  - Continue waiting for images")
    print("   [exit]  - Exit program")
    print("="*50)
    choice = input("Your choice: ").strip().lower()
    return choice

# Main processing loop
row_num = last_done

print("🚀 Starting enhanced image downloader with skip/exit features...")
print("📝 Instructions:")
print("   1. Google search will open automatically for each college with 'campus' keyword")
print("   2. Right-click on images and select 'Copy image address'")
print("   3. The URL will be automatically detected and downloaded")
print("   4. Press Enter to skip current image, type 'exit' to quit")
print("   5. All images will be saved regardless of size")
print("-" * 60)

try:
    while True:
        id_number = sheet[f"A{row_num}"].value
        college_name_c = sheet[f"C{row_num}"].value
        college_name_d = sheet[f"D{row_num}"].value
        
        if id_number is None:  # End of file
            print("🎉 All rows processed successfully!")
            break
        
        if not college_name_c and not college_name_d:
            print(f"⚠️ Skipping ID {id_number} (no college name)")
            row_num += 1
            continue
        
        # Create folder for this ID
        folder_path = os.path.join(save_dir, str(id_number))
        os.makedirs(folder_path, exist_ok=True)
        
        # Check existing images
        existing_images = len([f for f in os.listdir(folder_path) 
                              if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
        
        if existing_images >= 3:
            print(f"⏩ Skipping {id_number} (already has {existing_images} images)")
            row_num += 1
            continue
        
        # Combine college names
        college_name = f"{college_name_c or ''} {college_name_d or ''}".strip()
        
        print(f"\n🏫 Processing ID: {id_number} | College: {college_name}")
        print(f"📊 Progress: Row {row_num} | Need {3 - existing_images} more images")
        
        if college_name:
            google_search_large_images(college_name)
            time.sleep(2)  # Give browser time to load
        
        count = existing_images
        consecutive_failures = 0
        
        while count < 3 and consecutive_failures < 3:
            print(f"\n📸 Getting image {count + 1}/3 for {id_number}...")
            
            # Wait for URL in clipboard with timeout
            url = wait_for_clipboard_url(timeout=60)
            
            if url == 'SKIP':
                print(f"⏭️ Skipping image {count + 1}")
                consecutive_failures = 0  # Reset failures when manually skipping
                break
            elif not url:
                print("⏰ No URL detected in 60 seconds.")
                choice = get_user_choice()
                
                if choice == 'exit':
                    print("🚪 Exiting program...")
                    # Save progress before exiting
                    with open(progress_file, "w") as f:
                        f.write(str(row_num))
                    exit(0)
                elif choice == 'wait':
                    continue
                else:  # Empty input or skip
                    print(f"⏭️ Skipping remaining images for {id_number}")
                    break
            else:
                # Download image
                img_name = f"{count + 1}.jpg"
                save_path = os.path.join(folder_path, img_name)
                
                if download_image(url, save_path):
                    count += 1
                    consecutive_failures = 0
                    print(f"✅ Successfully saved image {count}/3")
                else:
                    consecutive_failures += 1
                    print(f"❌ Failed to save image (attempt {consecutive_failures}/3)")
        
        # Save progress
        with open(progress_file, "w") as f:
            f.write(str(row_num + 1))
        
        print(f"📁 Completed ID {id_number}: {count} images saved")
        
        # Ask if user wants to continue to next college
        print(f"\n🔄 Ready to move to next college...")
        choice = input("Press Enter to continue, or type 'exit' to quit: ").strip().lower()
        if choice == 'exit':
            print("🚪 Exiting program...")
            break
        
        row_num += 1
        
        # Small delay between records
        time.sleep(1)

except KeyboardInterrupt:
    print("\n\n⛔ Program interrupted by user (Ctrl+C)")
    # Save progress
    with open(progress_file, "w") as f:
        f.write(str(row_num))
    print(f"💾 Progress saved at row {row_num}")

print("\n🏁 Process completed!")