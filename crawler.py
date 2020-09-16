import requests
from bs4 import BeautifulSoup
import json

url = 'https://weworkremotely.com/categories/remote-programming-jobs#job-listings'

def find_jobs():

    jobs_list = []

    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        jobs = soup.findAll('li')

        for job in jobs:
            company = job.find('span', class_ = "company")
            position = job.find('span', class_ = "title")
            format = job.find('span', class_ = "region company")
            date = job.find('span', class_ = 'date')

            if None in (company, position, format, date):
                continue

            print('Company:', company.text, '\nPosition:', position.text, '\nLocation:', format.text, '\nPublised Date:', date.text)
            print('--------------------------------')


            job_structure = {
                'company': company.text,
                'position': position.text,
                'format': format.text,
                'date': date.text
            }

            jobs_list.append(job_structure)

        return output_job(jobs_list)

    except Exception as e:
        print("crawling failed: ")
        print(e)

def output_job(jobs_list):
    with open("jobs.txt", 'w') as f:
        json.dump(jobs_list, f)

find_jobs()
