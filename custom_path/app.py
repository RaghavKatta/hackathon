from flask import Flask, render_template, request, jsonify
import osmnx as ox
import networkx as nx
import folium
import numpy as np
from folium.plugins import MeasureControl
import os



app = Flask(__name__)

graph = ox.load_graphml("nyc_walk.graphml")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map', methods=['GET'])
def map_view():
    path_finding()
    return render_template('map.html')  # Change this to map_view.html to avoid conflict

@app.route('/route', methods=['POST'])
def route():
    data = request.json
    start_lat, start_lon = data['start']
    end_lat, end_lon = data['end']

    # Find the nearest nodes to the start and end points
    start_node = ox.distance.nearest_nodes(graph, X=start_lon, Y=start_lat)
    end_node = ox.distance.nearest_nodes(graph, X=end_lon, Y=end_lat)

    # Find the shortest path using the A* algorithm
    route = nx.astar_path(graph, start_node, end_node, heuristic=None, weight='length')

    # Extract the latitude and longitude for each node in the route
    route_coords = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in route]

    return jsonify(route_coords)

def path_finding():
    # Get the start and end coordinates from the query parameters
    try:
        start_lat = float(request.args.get('start_lat'))
        start_lon = float(request.args.get('start_lon'))
        end_lat = float(request.args.get('end_lat'))
        end_lon = float(request.args.get('end_lon'))

        start_coords = (start_lat, start_lon)
        end_coords = (end_lat, end_lon)
    
    except:
        start_coords = (40.7128, -74.0060)  # Default to example coordinates in NYC
        end_coords = (40.730610, -73.935242)

    # Create a map centered around the start point
    m = folium.Map(location=start_coords, zoom_start=12)

    # Add markers for start and end points
    folium.Marker(start_coords, popup="Start", icon=folium.Icon(color='green')).add_to(m)
    folium.Marker(end_coords, popup="End", icon=folium.Icon(color='red')).add_to(m)

    start_node = ox.distance.nearest_nodes(graph, X=start_coords[1], Y=start_coords[0])
    end_node = ox.distance.nearest_nodes(graph, X=end_coords[1], Y=end_coords[0])

    # Calculate the shortest path
    route = nx.shortest_path(graph, start_node, end_node, weight='length')
    route_coords = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in route]

    # Add the route as a PolyLine on the map
    folium.PolyLine(route_coords, color="blue", weight=15.5, opacity=1).add_to(m)

    # Add a measure control to the map
    measure_control = MeasureControl(position='bottomleft', primary_length_unit='meters', secondary_length_unit='miles', primary_area_unit='sqmeters', secondary_area_unit='acres')
    m.add_child(measure_control)

    # Save the map as an HTML file in the static directory
    map_path = os.path.join('static', 'map1.html')
    m.save(map_path)

if __name__ == '__main__':
    app.run(debug=True)
