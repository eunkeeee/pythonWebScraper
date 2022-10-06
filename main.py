from flask import Flask, render_template, request
from extractors.weWorkRemotely import extract_wwr_jobs

app=Flask("jobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="nico")

@app.route("/search")
def search():
    keyword = request.args.get("keyword") # req.query
    jobs = extract_wwr_jobs(keyword)
    return render_template("search.html", keyword=keyword, jobs=jobs)

app.run("127.0.0.1")