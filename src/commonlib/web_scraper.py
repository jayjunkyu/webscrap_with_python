from bs4 import BeautifulSoup
import requests

from src.commonlib.constants import TIMESJOB_URL
from src.commonlib.utils import is_more_than_month_old


def find_jobs(start_page=1, end_page=1):
    print('Put some skill that you are not familiar with')
    unfamiliar_skill = input('>').strip().lower()
    print(f'Filtering out {unfamiliar_skill}')
    results = []

    for page in range(start_page, end_page + 1):
        html_text = requests.get(TIMESJOB_URL.format(page=page)).text
        soup = BeautifulSoup(html_text, features='lxml')
        jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

        for job in jobs:
            title = job.header.h2.a.text.strip()
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.strip().replace(' ', '')
            published_date = job.find('span', class_='sim-posted').text.strip().split('Posted')[-1]
            more_info = job.header.h2.a['href']

            if not is_more_than_month_old(published_date):
                break

            if unfamiliar_skill in skills.split(','):
                break

            results.append(
                f'''
            Company Name: {company_name}
            Title: {title}
            Required Skills: {skills}
            Published Date: {published_date}
            More info: {more_info}
            '''
            )

    return results
