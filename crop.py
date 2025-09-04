import os
from PIL import Image

base_dir = "Downloaded_Images"
target_w, target_h = 1200, 900

def resize_and_crop(image, target_w, target_h):
    """Resize proportionally and then center crop to exactly 1200x900 without padding."""
    w, h = image.size
    target_ratio = target_w / target_h
    img_ratio = w / h

    # First, scale up to cover target area without leaving gaps
    if img_ratio > target_ratio:
        # Image is wider than target — match height first
        new_height = target_h
        new_width = int(new_height * img_ratio)
    else:
        # Image is taller than target — match width first
        new_width = target_w
        new_height = int(new_width / img_ratio)

    image = image.resize((new_width, new_height), Image.LANCZOS)

    # Now center crop
    left = (new_width - target_w) / 2
    top = (new_height - target_h) / 2
    right = left + target_w
    bottom = top + target_h

    return image.crop((left, top, right, bottom))

for folder_name in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder_name)
    if not os.path.isdir(folder_path):
        continue

    print(f"\n📂 Processing folder: {folder_name}")

    images = [f for f in os.listdir(folder_path) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    images.sort()

    # Keep only the first 3 images
    for idx, img_name in enumerate(images):
        img_path = os.path.join(folder_path, img_name)

        if idx < 3:
            try:
                img = Image.open(img_path)
                cropped = resize_and_crop(img, target_w, target_h)
                new_path = os.path.join(folder_path, f"{idx+1}.jpg")
                cropped.save(new_path, quality=95)
                print(f"✅ Saved {new_path}")
                if img_path != new_path:  # Remove original if filename changed
                    os.remove(img_path)
            except Exception as e:
                print(f"❌ Error processing {img_name}: {e}")
        else:
            os.remove(img_path)
            print(f"🗑 Deleted extra image: {img_name}")

print("\n🎯 Done! Only 3 cropped images (1200×900px) per folder remain.")
