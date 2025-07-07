import pandas as pd
import folium
from geopy.geocoders import Nominatim
from time import sleep

# Load your CSV
df = pd.read_csv("venues.csv")

# Initialize map (centered on U.S.)
map = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

# Set up geocoder
geolocator = Nominatim(user_agent="venue-mapper")

# Loop through rows
for index, row in df.iterrows():
    venue = row['Venue']
    city = row['City']
    state = row['State']
    
    # First try: venue + city + state
    location_str = f"{venue}, {city}, {state}"
    print(f"📍 Trying to geocode: {location_str}")
    
    try:
        location = geolocator.geocode(location_str)
        if not location:
            # Retry without venue
            fallback_str = f"{city}, {state}"
            print(f"⚠️ Couldn't find venue, retrying with fallback: {fallback_str}")
            location = geolocator.geocode(fallback_str)
        
        if location:
            folium.Marker(
                location=[location.latitude, location.longitude],
                popup=f"<b>{venue}</b><br>{city}, {state}",
                tooltip=venue
            ).add_to(map)
            print(f"✅ Plotted: {venue} in {location.address}")
        else:
            print(f"❌ Couldn't geocode either '{location_str}' or fallback '{fallback_str}'")
            
    except Exception as e:
        print(f"❌ Error geocoding '{location_str}': {e}")
    
    sleep(1)  # To respect Nominatim's rate limits


# Save map to HTML file
map.save("venue_map.html")
print("✅ Map saved to venue_map.html")
