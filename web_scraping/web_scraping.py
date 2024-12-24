import requests
from bs4 import BeautifulSoup

URL = "https://wandertaj.netlify.app/"

page= requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")
res = soup.find(class_="sec-quotes").text
link = soup.find("a", class_="cv-btn-theme")
if link:  # Ensure the link exists
    print(link['href'])

print(res)
print(soup.title.text)
# print(page.text)

for data in link:
    print(data)