import requests
from bs4 import BeautifulSoup


def getData():
    baseurl = "https://www.dreamjob.ma/"
    jobs = []

    resp = requests.get(baseurl)
    soup = BeautifulSoup(resp.text, 'html.parser')

    articl = soup.find_all("h3", attrs={"class": "jeg_post_title"})
    

    for job in articl:
        title = job.text.strip()
        url = job.findChild("a")['href']
        jobs.append({"title":title,"url":url})
    
    return jobs

# print(articl[0].findChild("a")['href'])
