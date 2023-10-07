from flask import Flask, render_template, request, redirect, url_for
import folium

app = Flask(__name__)

@app.route('/')
def index():
    # Create the map object
    m = folium.Map(location=[-0.023559, 37.906193], zoom_start=7, tiles='Stamen Terrain')

    # Add marker to the map
    folium.Marker(location=[-1.292066, 36.821945], popup='Nairobi', icon=folium.Icon(icon='cloud')).add_to(m)

    # Render the map
    m.get_root().render()

    # Derive the script and style tags to be rendered in the template
    header = m.get_root().header.render()

    # Derive the div tag to be rendered in the html body
    body_html = m.get_root().html.render()

    # Derive the script tag to be rendered in the html body
    script = m.get_root().script.render()

    return render_template('index.html', header=header, body_html=body_html, script=script)

@app.route('/map')
def display_map():
    return render_template('map.html')

@app.route('/about')
def user(name):
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)