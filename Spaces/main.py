from flask import Flask, render_template, url_for
import folium

app = Flask(__name__)

#Generating a map of Kenya and saving it 
m = folium.Map(location=[0.0236, 37.9062], zoom_start=12)

m.save(outfile= 'templates/map.html')

ngong = folium.Map(location=[1.3090, 36.7492], zoom_start=10)
ngong.save(outfile= 'templates/ngong.html')

kakamega = folium.Map(location=[0.2913, 34.8565], zoom_start=10)
kakamega.save(outfile= 'templates/kakamega.html')

karura = folium.Map(location=[1.2407, 36.8304], zoom_start=10)
karura.save(outfile= 'templates/karura.html')

aberdare = folium.Map(location=[0.4517, 36.7388], zoom_start=10)
aberdare.save(outfile= 'templates/aberdare.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map/')
def map():
    return render_template('map.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/ngong/')
def login():
    return render_template('ngong.html')

@app.route('/register/')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug = True)
