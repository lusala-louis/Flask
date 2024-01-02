import os
from flask import Flask, render_template, request, redirect, url_for
import folium
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAchemy(app)
Bootstrap(app)

class Sensors(db.Model):
    __tablename__ = 'sensors'
    id = db.Column(db.Integer, primary_key = True)
    forest = db.Column(db.String(64))
    latitude = db.Column(db.Float(64))
    longitude = db.Column(db.Float(64))

    def __repr__(self):
        return '<Sensor %r>' % self.forest

class Tracking(db.Model):
    __tablename__ = 'sounds'
    sensors_id = db.Column(db.Integer, db.ForeignKey(sensors.id))
    

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