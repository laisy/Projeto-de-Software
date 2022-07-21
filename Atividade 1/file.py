from bs4 import BeautifulSoup

import requests

def getWebText(url):
    try:
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')

        return [x.extract().getText() for x in soup.findAll('p')]
    except Exception as e:
        raise e
