from flask import Flask, request, render_template, jsonify
import json, math
# from flask.ext.googlemaps import GoogleMaps
app = Flask(__name__)
f = open('object.json', 'r')
data = json.load(f)
#print(data)
# @app.route("/")
# def main():
#     return render_template('testmap.html')

# if __name__ == "__main__":
#     app.run()
#########################
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['searchitem']
    processed_text = text.upper()
    return render_template("index.html", value = processed_text)

@app.route('/get', methods=['GET'])
def get_closest_park():
    location = [float(i) for i in request.args.get('location').split(',')]
    distance = float(request.args.get('distance'))
    tmp = []
    for p in data:
        d = get_distance([p["x_coord"], p["y_coord"]], location)
        if d < distance:
            tmp.append(p)
    return jsonify(tmp)

def get_distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

if __name__ == "__main__":
    app.run()
######################
# @app.route("/")
# def main():
#     return render_template('testmap.html')

# if __name__ == "__main__":
#     app.run()
###########################
# from flask import Flask, request, render_template

# app = Flask(__name__)

# @app.route('/')
# def my_form():
#     return render_template('my-form.html')

# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return render_template("my-form.html", value = processed_text)