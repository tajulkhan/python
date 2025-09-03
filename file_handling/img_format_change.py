import os
from PIL import Image
import pillow_avif  # enables AVIF support in Pillow

# Base folder where your folders are
base_folder = r"D:\CityWebShops\AllFolders"

# Final extension
final_ext = ".jpg"

# Extensions we want to convert
convert_exts = [".png", ".webp", ".gif", ".bmp", ".tiff", ".jpeg", ".jpg", ".avif"]

for root, dirs, files in os.walk(base_folder):
    for file in files:
        file_path = os.path.join(root, file)
        ext = os.path.splitext(file)[1].lower()

        # If it's already .jpg → keep
        if ext == ".jpg":
            continue

        # If it's in convert list → convert
        if ext in convert_exts:
            try:
                img = Image.open(file_path).convert("RGB")

                # Always save as .jpg
                new_file = os.path.splitext(file_path)[0] + final_ext

                # Special compression rules
                if ext == ".webp" or ext == ".avif":
                    img.save(new_file, "JPEG", quality=85, optimize=True)
                else:
                    img.save(new_file, "JPEG", quality=95, optimize=True)

                # Remove old file
                os.remove(file_path)

                print(f"✅ Converted: {file_path} → {new_file}")

            except Exception as e:
                print(f"⚠️ Could not convert {file_path}: {e}")

        else:
            print(f"❌ Skipped (unknown format): {file_path}")
