from bs4 import BeautifulSoup
import requests
import json
import os
import sys
import argparse

my_parser = argparse.ArgumentParser(description='Search for a job keyword')
my_parser.add_argument('Job keyword', metavar='jobkey', type=str, help='Job you want to search for')

args = my_parser.parse_args()
##### figure out how to parse the args after this section

url = 'https://www.monster.com/jobs/search/?q=Software-Developer'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

jobArr = []

job_elems = content.find_all('section', class_='card-content')
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    jobObj = {
        "title_elem": title_elem.text,
        "company_elem": company_elem.text,
        "location_elem": location_elem.text
    }
    jobArr.append(jobObj)

with open('jobData.json', 'w') as outfile:
    json.dump(jobArr, outfile)

    # print(title_elem.text)
    # print(company_elem.text)
    # print(location_elem.text)
    # print()

python_jobs = content.find_all('h2', string=lambda text: 'javascript' in text.lower())
print(len(python_jobs))

#print(job_elems.prettify())

# with open('tweetData.json', 'w') as outfile:
#     json.dump(tweetArray, outfile)




