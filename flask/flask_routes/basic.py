#!/usr/bin/env python3

from flask import Flask, render_template
import webbrowser

# automaticly opens web browser on the Flask server
webbrowser.open_new('http://127.0.0.1:5000')

app = Flask(__name__, template_folder="template")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/page/")
def page():
    return render_template("page.html")

if __name__ == "__main__":
    app.run()#(host="0.0.0.0", port=8080, debug=False)

