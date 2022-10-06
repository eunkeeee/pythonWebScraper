from flask import Flask

app=Flask("jobScrapper")

@app.route("/")
def home():
    return "hey there!" 

@app.route("/hello")
def hello():
    return 'hello you!'

app.run("127.0.0.1")