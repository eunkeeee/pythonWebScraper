from requests import get
from bs4 import BeautifulSoup
from extractors.weWorkRemotely import extract_wwr_jobs

keyword = input("What do you want to search for?")

jobs = extract_wwr_jobs(keyword)

file = open(f"{keyword}.csv", "w", encoding="utf-8")

# Write Header (seperated with comma)
file.write("Position,Company,Location,URL\n")

for job in jobs:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")
file.close()