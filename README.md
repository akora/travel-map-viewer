# Travel Maps Viewer

A Flask-based web application for visualizing travel history using Google Maps and local GeoJSON data. The application allows you to view visited cities and countries on interactive maps while minimizing API usage through local data storage.

## Project Structure

```text
travel_maps/
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables (API keys)
├── static/
│   ├── js/             # JavaScript files
│   └── data/
│       ├── visited_cities.json    # Cities data
│       ├── visited_countries.json # Countries data
│       └── geo-json/             # GeoJSON boundary files
│           ├── countries-all.geo.json  # All country boundaries
│           └── countries/        # Individual country/state files
└── templates/
    ├── base.html           # Base template with common layout
    ├── index.html          # Home page template
    ├── visited_cities.html # Cities view template
    └── visited_countries.html # Countries view template
```

## Setup Instructions

### 1. Python Virtual Environment

Create and activate a virtual environment:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 2. Install Dependencies

With the virtual environment activated:

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

1. Create a `.env` file in the project root (already done)
2. Add your Google Maps API keys to the `.env` file:

```text
GOOGLE_MAPS_API_KEY=your_api_key_here
GOOGLE_MAPS_MAP_ID=your_map_id_here  # For advanced markers
```

### 4. Running the Application

With the virtual environment activated:

```bash
python3 app.py
```

The application will be available at `http://127.0.0.1:5001`

## Features

### Global Features

- Interactive Google Maps integration with custom styling
- Modern, responsive design with navigation between views
- Local GeoJSON data storage for efficient loading
- Minimized Google Maps API usage

### Visited Cities View

- Interactive markers for each visited city
- Color-coded markers based on visit date
- Styled info windows with visit details
- Modern design with rounded corners and shadows
- Icons for visit dates and comments

### Visited Countries View

- Interactive country highlighting using GeoJSON boundaries
- Special handling for US states with individual state boundaries
- Auto-hiding sidebar with smooth transitions
- Country list with visit details and cities
- Smooth animations and transitions

## Managing Travel Data

### Cities Data

Cities data is stored in `static/data/visited_cities.json`. To add a new city:

1. Open `static/data/visited_cities.json`
2. Add a new entry to the "cities" array following this format:

```json
{
  "name": "City Name",
  "country": "Country Name",
  "coordinates": {
    "lat": 00.0000,  // Latitude
    "lng": 00.0000   // Longitude
  },
  "visitDate": "YYYY-MM-DD",
  "comment": "Optional comment about your visit"
}
```

### Countries Data

Countries data is stored in `static/data/visited_countries.json`. To add a new country:

1. Open `static/data/visited_countries.json`
2. Add a new entry to the "countries" array following this format:

```json
{
  "name": "Country Name",
  "code": "XXX",        // 3-letter country code (ISO 3166-1 alpha-3)
  "visitDate": "YYYY-MM-DD",
  "comment": "Optional comment about your visit",
  "cities": ["City1", "City2"],  // Cities visited in this country
  "states": ["XX", "YY"]         // Only for USA, state codes
}
```

To find coordinates for a city without using the Geocoding API:

1. Visit Google Maps (<https://www.google.com/maps>)
2. Right-click on the city
3. The coordinates will appear at the top of the context menu
4. Copy these numbers as lat/lng values

## Development

The application uses:

- Flask 3.0.0 for the web server
- Google Maps JavaScript API for map rendering
- Local GeoJSON files for country and state boundaries
- Advanced Markers for better performance and styling
- Custom CSS transitions for smooth animations

## Future Enhancements

- Timeline view of travels
- Travel statistics and analytics
- Country comparison features
- Photo integration
- Travel route visualization
- Filter by year or continent
- Country information integration

## Data Sources

The GeoJSON files used in this project for country and US state boundaries are sourced from:

- [OpenDataSoft World Administrative Boundaries dataset](https://public.opendatasoft.com/explore/dataset/world-administrative-boundaries/)
- [DataHub.io Country Polygons as GeoJSON](https://datahub.io/core/geo-countries)

This data is originally derived from [Natural Earth](http://www.naturalearthdata.com/) and is licensed under the [Open Data Commons Public Domain Dedication and License v1.0](http://opendatacommons.org/licenses/pddl/).
