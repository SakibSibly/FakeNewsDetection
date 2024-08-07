import requests
import os
from dotenv import load_dotenv


class CustomScraeper:
    def __init__(self, input_text: str) -> None:
        load_dotenv()
        self.API_KEY=os.getenv('API_KEY')
        self.SEARCH_ENGINE_ID=os.getenv('SEARCH_ENGINE_ID')
        self.FILE_PATH='ml/result.txt'
        self.URL=os.getenv('URL')
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
