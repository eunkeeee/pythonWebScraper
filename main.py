from flask import Flask, render_template

app=Flask("jobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="nico")

@app.route("/hello")
def hello():
    return 'hello you!'

app.run("127.0.0.1")