import pandas as pd
import requests
import time
from urllib.parse import urlencode

# Input & output files
input_file = r"D:abc/read.csv"
output_file = r"D:/abc/latitude-longitude/correct_coordinates.csv"

# Load CSV
df = pd.read_csv(input_file)

# Add empty columns if not present
if 'latitude' not in df.columns:
    df['latitude'] = None
if 'longitude' not in df.columns:
    df['longitude'] = None

# Function to get coordinates from Nominatim
def get_coordinates(row):
    # Build query string from available columns
    address_parts = [str(row.get(col, "")) for col in ["name", "street", "city", "pin_code"] if pd.notna(row.get(col))]
    query = " ".join(address_parts)

    if not query.strip():
        return None, None

    url = f"https://nominatim.openstreetmap.org/search?{urlencode({'q': query, 'format': 'json', 'limit': 1})}"
    headers = {"User-Agent": "Hotel-Geocoder/1.0 (test@gmail..com)"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data:
            return data[0]["lat"], data[0]["lon"]
    except Exception as e:
        print(f"Error fetching coordinates for {query}: {e}")
    return None, None

# Loop through rows
for idx, row in df.iterrows():
    if pd.isna(row['latitude']) or pd.isna(row['longitude']):
        lat, lon = get_coordinates(row)
        df.at[idx, 'latitude'] = lat
        df.at[idx, 'longitude'] = lon
        print(f"{idx}: {row.get('name', 'Unknown')} -> {lat}, {lon}")
        time.sleep(1)  # Respect Nominatim rate limit (max 1 request per second)

# Save updated CSV
df.to_csv(output_file, index=False)
print(f"✅ Updated file saved to {output_file}")
