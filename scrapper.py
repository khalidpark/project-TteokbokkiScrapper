import requests
from bs4 import BeautifulSoup

URL = f'https://www.mangoplate.com/search/%EB%96%A1%EB%B3%B6%EC%9D%B4?keyword=%EB%96%A1%EB%B3%B6%EC%9D%B4&page='

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  print(soup)
  pagination = soup.find("div", {"class" : "item_title"})

def get_lands():
    last_page = get_last_page()