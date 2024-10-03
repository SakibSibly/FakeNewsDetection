import requests
import os
import environ
from pathlib import Path


class CustomScraper:
    def __init__(self, input_text: str) -> None:
        self.env = environ.Env()
        BASE_DIR = Path(__file__).resolve().parent.parent
        environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
        self.API_KEY=self.env('API_KEY')
        self.SEARCH_ENGINE_ID=self.env('SEARCH_ENGINE_ID')
        self.FILE_PATH='ml/result.txt'
        self.URL=self.env('URL')
        self.params = {
            'key' : self.API_KEY,
            'cx' : self.SEARCH_ENGINE_ID,
            'q' : input_text,
            'num' : 10,
            'start' : 1
        }

    def getNews(self) -> None:
        cnt = 0
        for page in range(1, 11):
            res = requests.get(self.URL, params=self.params)
            if res.status_code == 200:
                res = res.json()
                items = res['items']

                for item in items:
                    cnt+=1
                    # site_name = '[' + item['pagemap']['metatags'][0]['og:site_name'] + ']'
                    site_name = "DUMMY_SITE_NAME" # Scraping insight needed
                    title = 'Title : ' + item['title']
                    snippet = 'Snippet : ' + item['snippet']
                    link = 'link : ' + item['link']
                    res = f"-->>{cnt}\n" + site_name + '\n' + title + '\n' + snippet + '\n' + link + '\n\n\n'
                    file = open(self.FILE_PATH, 'a', encoding='utf-8')
                    file.write(res)
                    file.close()

                self.params['start'] = self.params['start']+1
                # print("Page", page, "Checked!")
            else:
                # print("Sorry...Technical Problem!")
                break
