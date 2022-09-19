import requests
from bs4 import BeautifulSoup

URL = "https://www.placardefutebol.com.br/brasileirao-serie-a"

response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

tabela = soup.select_one("div.league-table")
rows = tabela.find_all("tr")

# remove o primeiro item, que é o cabeçalho da tabela
rows.pop(0)

data = []

for row in rows:
    tempData = {}

    texto = row.text.strip() # tira os espaços na lateral
    team_data = texto.split("\n") # separa os dados
    
    tempData["posicao"] = team_data[0]
    tempData["equipe"] = team_data[1]
    tempData["pontos"] = team_data[2]
    tempData["jogos"] = team_data[3]
    tempData["vitorias"] = team_data[4]
    tempData["empates"] = team_data[5]
    tempData["derrotas"] = team_data[6]
    tempData["saldo_gols"] = team_data[7]

    data.append(tempData)

print(data)

# for index in range(0, len(rows), 7):
#     temp_data = {}

#     temp_data["equipe"] = rows[index+data["equipe"]].text
#     print(temp_data)