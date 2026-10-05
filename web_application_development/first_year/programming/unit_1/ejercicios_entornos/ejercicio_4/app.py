from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>¡Bienvenid@ a mi aplicación Flask!</h1>"

@app.route("/saluda")
def saluda():
    return render_template("saluda.html")

if __name__ == "__main__":
    app.run(debug=True)
