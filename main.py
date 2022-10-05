from requests import get
from bs4 import BeautifulSoup
from extractors.weWorkRemotely import extract_wwr_jobs
from file import save_to_file

keyword = input("What do you want to search for?")
jobs = extract_wwr_jobs(keyword)

save_to_file(keyword,jobs)
