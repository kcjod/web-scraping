from bs4 import BeautifulSoup
import os
import pandas as pd

data = {'title':[],'price':[],'link': []}

for file in os.listdir("data"):
    with open(f"data/{file}") as f:
        try:
            html_doc = f.read()
            soup = BeautifulSoup(html_doc, 'html.parser')
            
            t = soup.find("h2")
            title = t.get_text()
            p = soup.find("span", attrs={'class': 'a-price-whole'})
            price = p.get_text()
            l = soup.find("a")['href']
            link = f"https://amazon.in/{l}"
            data['title'].append(title)
            data['price'].append(price)
            data['link'].append(link)
        except Exception as e:
            pass

df = pd.DataFrame(data=data)
df.to_csv("data.csv")