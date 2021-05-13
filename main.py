import csv
import requests
import pandas as pd
from config import URL, ARQUIVO_CSV

# Requisicao para o Link do arquivo .csv
response = requests.get(URL)
#print(response.content)


#Criando um arquivo chamado covid 19.csv e salvando no pc local
with open('covid19.csv', 'w', newline='\n') as novo_arquivo:
    writer = csv.writer(novo_arquivo)
    for linha in response.iter_lines():
        writer.writerow(linha.decode('utf-8').split(','))

# Abrir um arquivo .csv apartir do projeto raiz
with open(ARQUIVO_CSV) as arquivo:
    leitor_exemplo = csv.reader(arquivo)
    for linha in leitor_exemplo:
       # print(linha)
       # if linha[2]  == 'Brazil' and linha[3] == '2020-06-11':
       if linha[2] == 'Brazil':
            print(f"Linha # {leitor_exemplo.line_num} {linha[4]}")

#Usando o modulo Pandas para ler o arquivo .csv
arquivo_csv = pd.read_csv(ARQUIVO_CSV, usecols= ['location', 'date', 'total_cases', 'total_deaths'], index_col = 'date')

# Mostrando os 10 primeiros
print(arquivo_csv.head(10).to_string())
#print(arquivo_csv['location'].tail(20)) # ultimos 20
#print(arquivo_csv['location'].head(20)) #primeiros 20

# Filtrar os dados
print(arquivo_csv.loc[(arquivo_csv.location == 'Brazil') & (arquivo_csv.index == '2020-06-12')])