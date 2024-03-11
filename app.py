from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')  # domyślna strona startowa strona
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=False)
