from flask import *

app = Flask(__name__)

#ruta inicial
@app.route('/')
def home():
    return render_template("home.html")

#ruta about
@app.route('/about')
def about():
    return render_template("about.html")

#ruta contact
@app.route('/contact')
def about():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

