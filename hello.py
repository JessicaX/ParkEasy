from flask import Flask, request, render_template
# from flask.ext.googlemaps import GoogleMaps
app = Flask(__name__)

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