import os
from PIL import Image

# Base folder where your gesorteerd folders are
base_folder = r"D:\CityWebShops\wetransfer_b-b_2025-08-26_1901\B&B"

for root, dirs, files in os.walk(base_folder):
    for file in files:
        file_path = os.path.join(root, file)

        # If it's already a JPG → do nothing
        if file.lower().endswith(".jpg") or file.lower().endswith(".jpeg"):
            continue

        # If it's WEBP → convert to JPG
        if file.lower().endswith(".webp"):
            try:
                img = Image.open(file_path).convert("RGB")

                # New filename with .jpg extension
                new_file = os.path.splitext(file_path)[0] + ".jpg"

                # Save JPG version
                img.save(new_file, "JPEG", quality=95)

                # Remove old WEBP file
                os.remove(file_path)

                print(f"✅ Converted: {file_path} → {new_file}")

            except Exception as e:
                print(f"⚠️ Could not convert {file_path}: {e}")
