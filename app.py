from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)

def load_cities():
    with open('static/data/visited_cities.json', 'r') as f:
        return json.load(f)

def load_colors():
    with open('static/data/colors.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html', 
                         api_key=os.getenv('GOOGLE_MAPS_API_KEY'),
                         map_id=os.getenv('GOOGLE_MAPS_MAP_ID'))

@app.route('/visited-cities')
def visited_cities():
    cities = load_cities()
    colors = load_colors()
    return render_template('visited_cities.html',
                         cities=cities['cities'],
                         colors=colors,
                         api_key=os.getenv('GOOGLE_MAPS_API_KEY'),
                         map_id=os.getenv('GOOGLE_MAPS_MAP_ID'))

@app.route('/api/cities')
def get_cities():
    cities = load_cities()
    return jsonify(cities)

@app.route('/visited-countries')
def visited_countries():
    with open('static/data/visited_countries.json', 'r') as f:
        data = json.load(f)
    colors = load_colors()
    return render_template('visited_countries.html', 
                         api_key=os.getenv('GOOGLE_MAPS_API_KEY'),
                         map_id=os.getenv('GOOGLE_MAPS_MAP_ID'),
                         countries=data['countries'],
                         colors=colors)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
