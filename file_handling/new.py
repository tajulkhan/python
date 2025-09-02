import os

# Base folder where your "gesorteerd" folders are
base_folder = r"D:\CityWebShops\wetransfer_b-b_2025-08-26_1901\B&B"

for root, dirs, files in os.walk(base_folder):
    for folder in dirs:
        # If folder name starts with digits (ID)
        parts = folder.split(" ", 1)
        if parts[0].isdigit():
            old_path = os.path.join(root, folder)
            new_path = os.path.join(root, parts[0])

            if old_path != new_path:
                try:
                    os.rename(old_path, new_path)
                    print(f"✅ Renamed: {old_path} -> {new_path}")
                except Exception as e:
                    print(f"⚠️ Could not rename {old_path}: {e}")
