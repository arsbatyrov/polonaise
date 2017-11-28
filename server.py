from commonApi import CommonApi
from os import environ
import subprocess
import time
import flask
from flask import Flask, render_template
api = CommonApi("Poloniex")

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html', amount=api.MIN_AMOUNT, fee=api.FEE, profit=api.MIN_VALUE, losstime=api.LOSS_TIME)

@app.route("/parameters")
def parameters():
    return render_template('parameters.html', amount=api.MIN_AMOUNT, fee=api.FEE, profit=api.MIN_VALUE, losstime=api.LOSS_TIME)

@app.route('/yield')
def index():
    def inner():
        proc = subprocess.Popen(
            ['python main.py'],             #call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE
        )
        for line in iter(proc.stdout.readline,''):
            time.sleep(1)                           # Don't need this just shows the text streaming
            yield line.rstrip() + b'<br/>\n'
    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$


if __name__ == "__main__":
    port = int(environ.get("PORT", 5000))
    # host = str(environ.get("HOST", "0.0.0.0"))
    # app.run(host='0.0.0.0', port=port)
    app.run(port=port)