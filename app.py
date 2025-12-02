from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello DevOps from GDE student Péter!"

if __name__ == "__main__":
    # Itt indul el a web szerver
    app.run(host="0.0.0.0", port=8080)
