import requests

URL = "https://wandertaj.netlify.app/"
page= requests.get(URL)
print(page.text)