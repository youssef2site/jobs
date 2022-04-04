from scrap import getData
from flask import Flask, jsonify



app = Flask(__name__)

data = getData()

@app.route('/')
def hello():
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)