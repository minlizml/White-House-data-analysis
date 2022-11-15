import time
import requests
from bs4 import BeautifulSoup
import pandas as pd


data={
    'title':[],
    'type':[],
    'issue':[],
    'date':[]
}

page_num = 1
while True:
    print(f'Scraping page {page_num}...')

    response=requests.get(f'https://trumpwhitehouse.archives.gov/news/page/{page_num}')
    if response.status_code != 200:
        print('Ending...')
        break
    soup=BeautifulSoup(response.content,'html.parser')

    for article in soup.find_all('article'):
        article_class=article['class'][0]

        title = article.find('h2', class_= f"{article_class}__title").text.strip()
        type_ = article.find('p', class_=f"{article_class}__type")
        type_ = type_.text.strip() if type_ is not None else 'Other'
        issue=article.find('p', class_='issue-flag')
        issue=issue.text.strip() if issue is not None else 'Other'
        date=article.find('time').text.strip()

        data['title'].append(title)
        data['type'].append(type_)
        data['issue'].append(issue)
        data['date'].append(date)

    time.sleep(0.5)
    page_num += 1



print(len(data["title"]))
print(len(data["type"]))
print(len(data["issue"]))
print(len(data["date"]))

df = pd.DataFrame(data)
df.to_csv("data.csv")


