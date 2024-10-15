from bs4 import BeautifulSoup


with open("index.html") as f:
    html_doc = f.read()
    soup = BeautifulSoup(html_doc, "html.parser")

# print(soup.find_all("div"))

# print(soup.a.get("href"))
# print(soup.find(id="link3"))

# print(soup.select("div.italic"))
# print(soup.select("div#italic"))

# print(soup.find_all(class_="italic"))

# for child in soup.find(class_="container").children:
#     print(child)

for parent in soup.find(class_="box").parents:
    print(parent)