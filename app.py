from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run()
