from flask import Flask, render_template, request, redirect, url_for
import folium
from flask_bootstrap import Bootstrap
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

Bootstrap(app)

# Fetch the service account key
cred = credentials.Certificate('rangerAccountKey.json')

firebase_admin.initialize_app(cred, {'databaseURL': 'https://ranger-29fa1-default-rtdb.firebaseio.com/'})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def display_map():
    # Create the map object
    m = folium.Map(location=[-0.023559, 37.906193], zoom_start=3, height = 630, tiles='Stamen Terrain')

    # Add marker to the map
    folium.Marker(location=[13.021710, 74.793490], popup='Nairobi', icon=folium.Icon(icon='cloud')).add_to(m)

    # Render the map
    m.get_root().render()

    # Derive the script and style tags to be rendered in the template
    header = m.get_root().header.render()

    # Derive the div tag to be rendered in the html body
    body_html = m.get_root().html.render()

    # Derive the script tag to be rendered in the html body
    script = m.get_root().script.render()

    return render_template('map.html', header=header, body_html=body_html, script=script)

# Add routes for each forest page
@app.route('/forest/aberdare')
def aberdare_forest():
    return render_template('aberdare.html')  # Create aberdare.html with specific content

@app.route('/forest/ngong')
def ngong_forest():
    return render_template('ngong.html')  # Create ngong.html with specific content

@app.route('/about')
def user(name):
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)