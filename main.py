from src.commonlib.web_scraper import find_jobs

if __name__ == '__main__':
    try:
        end_page = int(input('Enter number of pages to scrap: ').strip())
        jobs = find_jobs(end_page=end_page)
        for job in jobs:
            print(job)
    except Exception as ex:
        print(f'{ex.__class__.__name__}: {ex.__str__()}')
