from flask import Flask, render_template, request
import sys


app = Flask(__name__)

@app.route("/")
def show_weather():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_weather():
    if request.method == "POST":
        return "test"


# don't change the following way to run flask:
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
