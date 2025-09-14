# csv_updater
import os
import pandas as pd

# Paths
base_folder = r"D:\ABC"
csv_file = r"D:\ABC\Sheet1.csv"
output_csv = r"D:\ABC\find_image_updated.csv"

# Load your CSV
df = pd.read_csv(csv_file)

# For each product_id, check images inside its folder
for i, row in df.iterrows():
    product_id = str(row['product_id'])
    folder_path = os.path.join(base_folder, product_id)

    if os.path.exists(folder_path):
        images = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(".jpg")])
        
        # Assign images to columns dynamically
        for idx, img in enumerate(images, start=1):
            col_name = f"img_{idx}"
            df.loc[i, col_name] = img
    else:
        print(f"⚠️ No folder for: {product_id}")

# Save updated CSV
df.to_csv(output_csv, index=False)
print(f"✅ Updated CSV saved at: {output_csv}")
