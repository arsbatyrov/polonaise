from commonApi import CommonApi
from os import environ
from flask import Flask, render_template
api = CommonApi("Poloniex")

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html', amount=api.MIN_AMOUNT, fee=api.FEE, profit=api.MIN_VALUE, losstime=api.LOSS_TIME)

@app.route("/parameters")
def parameters():
    return render_template('parameters.html', amount=api.MIN_AMOUNT, fee=api.FEE, profit=api.MIN_VALUE, losstime=api.LOSS_TIME)


if __name__ == "__main__":
    port = int(environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


# , api.MIN_AMOUNT, api.FEE, api.MIN_VALUE, api.LOSS_TIME