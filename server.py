from os import environ
from flask import Flask, render_template

app = Flask(__name__)
app.run(environ.get('5000'))

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()