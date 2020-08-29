#Importações
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

#1 - PEGAR A URL
url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'
req = requests.get(url)

#cria o objeto
soup = BeautifulSoup(req.content, 'html.parser')

#name_list = soup.find(class_='<select name=UF class="f1col">')

lista_uf = soup.find_all(class_='f1col')
#2 - Obtenha dados de pelo menos dois UFs, quanto mais, melhor(OK!):
for lista_td in lista_uf:
    lista = lista_td.find_all('option')
    for lista_dados in lista:
        if lista_dados.next_element.name == 'value':
            url_uf = '{0}{1}'.format(url, lista_dados.next_element.get('select'))
            print(url_uf)
        else:
            print(lista_dados.next_element)


lista_loc = soup.find_all(class_='f6col') #Se não encontrada NADA, retorna 'NONE'



#faixa_cep = soup.find_all('table', class_='tmptabela')
faixa_cep = soup.find_all("table", {"class": "tmptabela"})
for lista_f in faixa_cep:
    listaf = lista_f.find_all('tr')
    for lista_faixa in listaf:
        if lista_faixa.next_element.name == 'td':
            faixa_uf = '{0}{1}'.format(url, lista_faixa.next_element.get(''))
            print(faixa_uf)
        else:
            print(lista_faixa.next_element)

#print(lista_td)
print(lista_loc)
print(faixa_cep)



####------- Trás todos os links -------- #####
####all_links = soup.find_all("a")
####for link in all_links:
####    print (link.get("href"))
####-------------------------------------------------Fim

#soup.find('tbody') ---# tbody retorna uma matriz[], não usar!




