from flask import *

MkAir = Flask(__name__)

#ruta search
@app.route('/search')
def search():
    return render_template("/Python/search.html")

if __name__ == "__main__":
    app.run(debug=True)

