from flask import Flask, request
import subprocess

app = Flask(__name__)
@app.route('/', methods=['POST'])
def hello_world():
    subprocess.call(['/home/yuqi_tu/pullSimpleFlaskWebSite.sh'])
    return '{"status":"received"}'
if __name__ == '__main__':
    app.run()
