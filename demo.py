from flask import jsonify, Flask, escape, request, render_template

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('home.html')
@app.route('/speed')
def speed():
    return jsonify({"value":100})
@app.route('/sun')
def sun():
    return jsonify(100)
