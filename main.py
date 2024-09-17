import folium

# List of locations with their coordinates
locations = [
    {'state': 'Alabama', 'city': 'Birmingham', 'lat': 33.5186, 'lon': -86.8104},
    {'state': 'Arizona', 'city': 'Phoenix', 'lat': 33.4484, 'lon': -112.0740},
    {'state': 'Arkansas', 'city': 'Little Rock', 'lat': 34.7465, 'lon': -92.2896},
    {'state': 'California', 'city': 'San Diego', 'lat': 32.7157, 'lon': -117.1611},
    {'state': 'Colorado', 'city': 'Denver', 'lat': 39.7392, 'lon': -104.9903},
    {'state': 'DC', 'city': 'District of Columbia', 'lat': 38.9072, 'lon': -77.0369},
    {'state': 'Florida', 'city': 'Jacksonville', 'lat': 30.3322, 'lon': -81.6557},
    {'state': 'Florida', 'city': 'Tampa', 'lat': 27.9506, 'lon': -82.4572},
    {'state': 'Florida', 'city': 'Orlando', 'lat': 28.5383, 'lon': -81.3792},
    {'state': 'Florida', 'city': 'Miami', 'lat': 25.7617, 'lon': -80.1918},
    {'state': 'Georgia', 'city': 'Augusta', 'lat': 33.4735, 'lon': -82.0105},
    {'state': 'Louisiana', 'city': 'Baton Rouge', 'lat': 30.4515, 'lon': -91.1871},
    {'state': 'Maine', 'city': 'Portland', 'lat': 43.6591, 'lon': -70.2568},
    {'state': 'Missouri', 'city': 'Kansas City', 'lat': 39.0997, 'lon': -94.5786},
    {'state': 'Nevada', 'city': 'Las Vegas', 'lat': 36.1699, 'lon': -115.1398},
    {'state': 'New Mexico', 'city': 'Albuquerque', 'lat': 35.0844, 'lon': -106.6504},
    {'state': 'North Carolina', 'city': 'Charlotte', 'lat': 35.2271, 'lon': -80.8431},
    {'state': 'North Carolina', 'city': 'Chapel Hill', 'lat': 35.9132, 'lon': -79.0558},
    {'state': 'North Carolina', 'city': 'Greenville', 'lat': 35.6127, 'lon': -77.3664},
    {'state': 'Ohio', 'city': 'Cleveland', 'lat': 41.4993, 'lon': -81.6944},
    {'state': 'Pennsylvania', 'city': 'Philadelphia', 'lat': 39.9526, 'lon': -75.1652},
    {'state': 'South Carolina', 'city': 'Columbia', 'lat': 34.0007, 'lon': -81.0348},
    {'state': 'Tennessee', 'city': 'Nashville', 'lat': 36.1627, 'lon': -86.7816},
    {'state': 'Texas', 'city': 'Houston', 'lat': 29.7604, 'lon': -95.3698},
    {'state': 'Texas', 'city': 'Fort Worth', 'lat': 32.7555, 'lon': -97.3308},
    {'state': 'Texas', 'city': 'Dallas', 'lat': 32.7767, 'lon': -96.7970},
    {'state': 'Texas', 'city': 'Corpus Christi', 'lat': 27.8006, 'lon': -97.3964},
    {'state': 'Utah', 'city': 'Salt Lake City', 'lat': 40.7608, 'lon': -111.8910},
    {'state': 'Virginia', 'city': 'Norfolk', 'lat': 36.8508, 'lon': -76.2859},
    {'state': 'Virginia', 'city': 'Richmond', 'lat': 37.5407, 'lon': -77.4360},
]

# Create a map centered on the United States
us_map = folium.Map(location=[37.0902, -95.7129], zoom_start=5)

# Add markers to the map
for loc in locations:
    folium.Marker(
        location=[loc['lat'], loc['lon']],
        popup=f"{loc['city']}, {loc['state']}",
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(us_map)

# Save the map to an HTML file
us_map.save('us_map_with_pins.html')

print("Map has been created and saved to 'us_map_with_pins.html'")