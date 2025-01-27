locations = {
    "city": "New York",
    "country": "USA",
    "continent": "North America"
}
if 'city' in locations:
    locations['location'] = locations.pop('city')
    print(f"Dictionary after renaming 'city' to 'location': {locations}")
else:
    print("Key 'city' not found in the dictionary.")