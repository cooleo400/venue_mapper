import pandas as pd
import folium
from geopy.geocoders import Nominatim
from time import sleep
import sys

# Get CSV filename from command line argument or use default
csv_filename = sys.argv[1] if len(sys.argv) > 1 else "venues.csv"

# Load your CSV
df = pd.read_csv(csv_filename)
print("Loading venues from: {}".format(csv_filename))
print("Found {} venues to process".format(len(df)))

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
    location_str = "{}, {}, {}".format(venue, city, state)
    print("Trying to geocode: {}".format(location_str))
    
    try:
        location = geolocator.geocode(location_str)
        if not location:
            # Retry without venue
            fallback_str = "{}, {}".format(city, state)
            print("Couldn't find venue, retrying with fallback: {}".format(fallback_str))
            location = geolocator.geocode(fallback_str)
        
        if location:
            folium.Marker(
                location=[location.latitude, location.longitude],
                popup="<b>{}</b><br>{}, {}".format(venue, city, state),
                tooltip=venue
            ).add_to(map)
            print("Plotted: {} in {}".format(venue, location.address))
        else:
            print("Couldn't geocode either '{}' or fallback '{}'".format(location_str, fallback_str))
            
    except Exception as e:
        print("Error geocoding '{}': {}".format(location_str, e))
    
    sleep(1)  # To respect Nominatim's rate limits


# Save map to HTML file
map.save("venue_map.html")
print("Map saved to venue_map.html")
