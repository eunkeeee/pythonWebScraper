from flask import Flask, render_template, request
from extractors.weWorkRemotely import extract_wwr_jobs
from extractors.remoteok import extract_remoteok_jobs

app=Flask("jobScrapper")

db={}

@app.route("/")
def home():
    return render_template("home.html", name="nico")

@app.route("/search")
def search():
    keyword = request.args.get("keyword") # req.query
    print("!!!KEYWORD:", keyword)
    if keyword in db: 
        jobs = db[keyword]
    else:
        jobs = extract_wwr_jobs(keyword)+extract_remoteok_jobs(keyword)
        db[keyword]=jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

app.run("127.0.0.1")
