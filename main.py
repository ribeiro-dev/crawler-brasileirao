import requests
from bs4 import BeautifulSoup

URL = "https://www.placardefutebol.com.br/brasileirao-serie-a"

response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

tabela = soup.select_one("div.league-table")
rows = tabela.find_all("tr")
