#Fonte: https://docs.python.org/pt-br/3/library/urllib.html
#serve para analisar url's
from urllib.parse import urlencode
from urllib.request import Request, urlopen
###Parsear pelo Beautiful - retorna os dados parseados do html mais legivel
from bs4 import BeautifulSoup
import json


#realizando agora a requisição
#PEGAR A URL
url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'
post_fields = {'relaxation': '17509140','Localidade': 'Marília', 'UF': 'SP'}


request= Request(url, urlencode(post_fields).encode())
result = urlopen(request).read()
result = str(result)

##string_vazia = ''


#ELIMINANDO CARACTERES DE SCAPE
def string_scape(s):
    s = s.replace('\\r','')
    s = s.replace('\\t','')
    s = s.replace('\\n', '')
    return s

def xml_scape(s):
    s = s.replace(u'["&lt", "&gt", "$amp", "&nbsp"]', '')
    return s

result = string_scape(result)
result = bytes(result,"iso-8859-1").decode('unicode_escape')
result = xml_scape(result)


#Usar um find - para pegar o que importa:
find = 'Localidade:</th>'
posicao = result.index(find) + len(find)
texto = result[posicao : posicao * 200] 

print(result)




