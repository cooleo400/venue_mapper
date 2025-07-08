# Venue Mapper

A Python script that creates an interactive map of music venues from the "Places to Play" Google Sheet data using geocoding and the Folium mapping library.

## Overview

This tool reads venue data from a CSV export of the "Places to Play" Google Sheet, geocodes the locations using OpenStreetMap's Nominatim service, and generates an interactive HTML map showing all the venues as clickable markers.

## Data Source

The venue data comes from the **"Places to Play" Google Sheet** - a crowdsourced database of music venues and festivals. To use this script:

1. **Access the Google Sheet**: Open the "Places to Play" Google Sheet
2. **Download as CSV**: Go to `File > Download > Comma-separated values (.csv)`
3. **Save the file**: Save it in the same directory as this script
4. **Run the script**: Use the downloaded CSV file as a parameter

## Features

- 🗺️ **Interactive Map**: Creates a Folium map with clickable venue markers
- 📍 **Smart Geocoding**: Attempts to geocode venues with fallback to city-level locations
- 🔄 **Error Handling**: Gracefully handles geocoding failures and provides feedback
- ⏱️ **Rate Limiting**: Respects Nominatim's rate limits with built-in delays
- 📊 **Progress Tracking**: Shows real-time geocoding progress in the console
- 📁 **Flexible Input**: Accepts any CSV file from the "Places to Play" sheet

## Prerequisites

### Python Version
This script requires **Python 3.6+** (tested with Python 3.10.7)

### Required Python Packages

Install the required dependencies using pip:

```bash
pip install pandas folium geopy
```

## Usage

### Step 1: Download the Data
1. Open the "Places to Play" Google Sheet
2. Go to `File > Download > Comma-separated values (.csv)`
3. Save the CSV file (e.g., as `places_to_play.csv`)

### Step 2: Run the Script

**With a specific CSV file** (recommended):
```bash
python map_venues.py "places_to_play.csv"
python map_venues.py "Places To Play _ Venues - Sheet1.csv"
```

**Using the default venues.csv** (if you rename your file):
```bash
python map_venues.py
```

### Step 3: View the Results
1. The script will display real-time progress in the terminal
2. Open the generated `venue_map.html` file in your web browser
3. Explore the interactive map with venue markers

## Expected CSV Format

The script expects the CSV to have these columns from the "Places to Play" Google Sheet:
- `Venue`: Name of the venue
- `City`: City where the venue is located  
- `State`: State or province

**Example from "Places to Play" data:**
```csv
State,City,Venue,Person of Contact - Name,Person of Contact - Email,Additional Notes,Url,Referral
California,Quincy,High Sierra Festival,,,,https://www.highsierramusic.com/,
Maine,Brunswick,Thomas Point Beach Bluegrass Festival,Shari Elder,sharilelder@gmail.com,"Contact info",https://www.thomaspointbeachbluegrass.com/,Tom Feeley
```

> **Note**: Additional columns are preserved but only `Venue`, `City`, and `State` are required for mapping.

## How It Works

### Console Output Example
```
Loading venues from: places_to_play.csv
Found 45 venues to process
Trying to geocode: High Sierra Festival, Quincy, California
Couldn't find venue, retrying with fallback: Quincy, California
Plotted: High Sierra Festival in Quincy, Plumas County, California, United States
Trying to geocode: Club Passim, Cambridge, Massachusetts
Plotted: Club Passim in Club Passim, Palmer Street, Cambridge, Massachusetts, United States
...
Map saved to venue_map.html
```

### Geocoding Strategy

The script uses a two-tier geocoding approach:

1. **Primary attempt**: Tries to geocode using the full venue name + city + state
2. **Fallback**: If the venue-specific geocoding fails, falls back to city + state

This ensures maximum accuracy while providing reasonable fallback locations for venues that can't be found specifically.

### Map Features

- **Interactive markers**: Click to see venue details
- **Tooltips**: Hover to see venue names
- **Responsive design**: Works on desktop and mobile
- **Zoom and pan**: Explore different regions

## Output Files

- `venue_map.html`: Interactive map file that opens in any web browser

## Troubleshooting

### Common Issues

1. **Missing packages**: Install required packages
   ```bash
   pip install pandas folium geopy
   ```

2. **File not found**: Ensure your CSV file path is correct
   ```bash
   python map_venues.py "path/to/your/downloaded_file.csv"
   ```

3. **Python version**: Use Python 3.6+ (check with `python --version`)

4. **Geocoding failures**: Some venues may not be found, but the script will:
   - Try fallback city-level geocoding
   - Log failed attempts to the console
   - Continue processing remaining venues

### Data Quality Tips

- Ensure venue names, cities, and states are spelled correctly in the Google Sheet
- Check for missing data (empty cells) which may cause geocoding issues
- The script handles missing data gracefully but may produce unexpected results

## Example Commands

```bash
# Using the downloaded Google Sheet CSV
python map_venues.py "Places To Play _ Venues - Sheet1.csv"

# If you renamed the file
python map_venues.py "my_venues.csv"

# Using default filename (if your CSV is named venues.csv)
python map_venues.py
```

## Customization

You can modify the script to:
- Change the map center location
- Adjust geocoding delays for rate limiting
- Customize marker appearance
- Modify popup content

## Contributing

This tool is designed to work specifically with the "Places to Play" Google Sheet format. If the sheet structure changes, the script may need updates to accommodate new column names or data formats.

## License

This project is open source. Feel free to modify and distribute as needed.
