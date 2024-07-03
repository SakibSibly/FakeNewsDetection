from django.shortcuts import render
from django.views import View
import requests
import os
from dotenv import load_dotenv
# Create your views here.

load_dotenv()


API_KEY = os.getenv("API_KEY")
SEARCH_ENGINE_ID=os.getenv('SEARCH_ENGINE_ID')
URL=os.getenv('URL')

    
class News:
    def scrap(query):

        params = {
                'key': API_KEY,
                'cx': SEARCH_ENGINE_ID,
                'q': query,
                'num': 10,
                'start': 1
            }
        
        for page in range(1, 11):
            res = requests.get(URL,params=params)
            print(page)
            if res.status_code == 200:
                res = res.json()
                items = res['items']

                for item in items:

                    # site_name = item['pagemap']['metatags'][0]['og:site_name']
                    # title = item['title']
                    # snippet = item['snippet']
                    # link = item['link']

                    site_name = item.get('pagemap', {}).get('metatags', [{}])[0].get('og:site_name', 'Unknown Site')
                    title = item.get('title', 'No Title')
                    snippet = item.get('snippet', 'No Snippet')
                    link = item.get('link', 'No Link')

                    news = f"{site_name}\n{snippet}\n\n"

                    file = open("result.txt",'a',encoding='UTF-8')
                    file.write(news)
                    file.close()



                params['start'] += 1

            else:
                print("You may run out of your api limit! \n\nPlease Change the api or upgrade plan!")
                return -1

    def summarize():
        pass

    def context_match():
        pass


class MainView(View):

    def showHomePage(request):
        if request.method == 'POST':
            query = request.POST.get('query')

            if query:
                value = News.scrap(query)
                if(value == -1):
                    content = "You may run out of your api limit! \n\nPlease Change the api or upgrade plan!"
                else:
                    file = open("result.txt",'r',encoding="UTF-8")
                    content = file.read()
                    file.close()
            else:
                content = "No News to Find!"

            return render(request,'home/show.html',{'content':content})

        return render(request, 'home/index.html')

