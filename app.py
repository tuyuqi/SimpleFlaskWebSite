from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return 'HAHAHAHAHHAHA'

if __name__ == '__main__':
    app.run()
