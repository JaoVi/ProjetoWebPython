from flask import Flask 

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1> Olá, Mundo!</h1>"

app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)