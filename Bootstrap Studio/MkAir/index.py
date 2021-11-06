from flask import *

MkAir = Flask(__name__)

#ruta search
@MkAir.route('/search')
def search():
    return render_template("search.html")

if __name__ == "__main__":
    MkAir.run(debug=True)

