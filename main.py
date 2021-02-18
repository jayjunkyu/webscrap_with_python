from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, features='lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    company_name = job.find('h3', class_='joblist-comp-name').text.strip()
    skills = job.find('span', class_='srp-skills').text.strip()
    published_date = job.find('span', class_='sim-posted').text.strip().split('Posted')[-1]

    if 'days' not in published_date:
        break

    print(f'''
    Company Name: {company_name}
    Required Skills: {skills}
    Published Date: Posted{published_date}
    ''')
