import zipfile
import pandas as pd
import base64
from pathlib import Path
import folium
from folium.plugins import MarkerCluster

# Paths to files
avatars_zip_path = 'data/avatars.zip'  # Replace with the path to your avatars zip file
csv_file_path = 'data/final.csv'  # Replace with the path to your CSV file
avatars_extract_path = 'extracted_avatars/'

# Extract avatars
with zipfile.ZipFile(avatars_zip_path, 'r') as zip_ref:
    zip_ref.extractall(avatars_extract_path)

# Load CSV file
csv_data = pd.read_csv(csv_file_path)

# Encode avatar images in base64 for displaying on the map
avatar_images = {
    img.stem: base64.b64encode(img.read_bytes()).decode('utf-8')
    for img in Path(avatars_extract_path).glob("*.png")
}

# Calculate map center based on CSV coordinates
min_lat, max_lat = csv_data['lat'].min(), csv_data['lat'].max()
min_lon, max_lon = csv_data['lon'].min(), csv_data['lon'].max()
map_center = [(min_lat + max_lat) / 2, (min_lon + max_lon) / 2]

# Initialize map with clustering
europe_map = folium.Map(location=map_center, zoom_start=4)
marker_cluster = MarkerCluster().add_to(europe_map)

# Loop through CSV entries and add markers with avatars
for _, row in csv_data.iterrows():
    name = f"{row['name.title']} {row['name.first']} {row['name.last']}"
    city = row['city']
    country_code = row['code']
    timezone = row['timezone']
    lat, lon = row['lat'], row['lon']
    avatar_key = row['avatar']

    # Include avatar image if available
    img_html = ""
    if avatar_key in avatar_images:
        img_html = f'<img src="data:image/png;base64,{avatar_images[avatar_key]}" width="50" height="50"><br>'

    # Define popup content
    popup_content = f"""
    {img_html}
    <b>{name}</b><br>
    City: {city}<br>
    Country Code: {country_code}<br>
    Timezone: {timezone}
    """

    # Add marker to the cluster
    folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(popup_content, max_width=200),
        tooltip=city
    ).add_to(marker_cluster)

# Save the map
europe_map.save('webpage/index.html')
