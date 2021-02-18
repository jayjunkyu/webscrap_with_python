from src.commonlib.web_scraper import find_jobs
import time

if __name__ == '__main__':
    end_page = int(input('Enter number of pages to scrap: ').strip())
    print('Put some skill that you are not familiar with')
    unfamiliar_skill = input('>').strip().lower()
    print(f'Filtering out {unfamiliar_skill}')
    while True:
        try:
            jobs = find_jobs(end_page=end_page, unfamiliar_skill=unfamiliar_skill)
            for job in jobs:
                print(job)
            time_wait = 10  # TODO: make this optional
            print(f'Waiting {time_wait} seconds.')
            time.sleep(time_wait)
            # TODO: export jobs into a csv file
            # TODO: add relevant unit tests
        except Exception as ex:
            print(f'{ex.__class__.__name__}: {ex.__str__()}')
            break
