from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/map/')
def map():
    return render_template('map.html')

@app.route('/timboroa')
def timboroa():
    return render_template('timboroa.html')

@app.route('/kakamega')
def kakamega():
    return render_template('kakamega.html')

@app.route('/karura')
def karura():
    return render_template('karura.html')

@app.route('/aberdares')
def aberdares():
    return render_template('aberdare.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/data/', methods = ['GET', 'POST'])
def basic():
    if method == 'POST':
        location = db.child('location').get().val()
        return location.val()

if __name__ == '__main__':
    app.run(debug = True)
