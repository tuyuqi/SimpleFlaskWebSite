from flask import Flask, request
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template("home.html")

if __name__ == '__main__':
    app.run()
