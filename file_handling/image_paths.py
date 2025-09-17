import pandas as pd

# File paths
campings_file = r"D:\CityWebShops\campings.csv"
images_file = r"D:\CityWebShops\find_image_updated.csv"
output_file = r"D:\CityWebShops\campings_with_image_urls.csv"

# Base URL
base_url = "http://localhost/wordpress/wp-content/uploads/Import"

# Load both CSVs
campings_df = pd.read_csv(campings_file)
images_df = pd.read_csv(images_file)

# Fix column names
images_df.rename(columns={images_df.columns[0]: "business_product_id"}, inplace=True)
campings_df.rename(columns={campings_df.columns[0]: "business_product_id"}, inplace=True)

# Merge them
merged_df = campings_df.merge(images_df, on="business_product_id", how="left")

# Convert image names to full URLs
for col in merged_df.columns:
    if col.startswith("img_"):
        merged_df[col] = merged_df.apply(
            lambda row: f"{base_url}/{row['business_product_id']}/{row[col]}" if pd.notna(row[col]) else "",
            axis=1
        )

# Save updated CSV
merged_df.to_csv(output_file, index=False)
print(f"✅ Updated CSV saved at: {output_file}")
