from flask import Flask, request, render_template, jsonify
import json, math, requests
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
@app.route('/')
def main():
    tmp = []    
    text = request.args.get('searchitem')
    print("text", text)
    if not text:
        print("here", text)    
        return render_template("index.html", value = text, points=json.dumps(tmp))
    processed_text = text.upper()
    location = [float(i) for i in text.split(',')]
    distance = float(request.args.get('distance'))/1000 if request.args.get('distance') else 0.1
    carpark_info = get_car_park_information()
    for p in data:
        d = get_distance([p["x_coord"], p["y_coord"]], location)
        if p["car_park_no"] in carpark_info and int(carpark_info[p["car_park_no"]]["lots_available"]) > 0: 
            print("here")
            p["distance"] = d
            p["info"] = carpark_info[p["car_park_no"]]
            tmp.append(p)
    tmp = sorted(tmp, key=lambda x: x["distance"])[:5]
    return render_template("index.html", value = processed_text, points=json.dumps(tmp), md=tmp[-1]["distance"])

def get_car_park_information():
    r = requests.get("https://api.data.gov.sg/v1/transport/carpark-availability")
    data = json.loads(r.text)
    tmp = {}
    for ci in data["items"][0]["carpark_data"]:
        print(ci)
        tmp[ci["carpark_number"]] = ci["carpark_info"][0]
    print(tmp)
    return tmp

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