import json
import re
import requests

def consulta(cep):
    cep = cep.replace('-', '')
    url = f'http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm'
    headers = {'User-Agent': 'Autociencia/1.0'}
    resposta = requests.request('GET', url, headers=headers)
    conteudo = resposta.content.decode('utf-8')
    resposta.close()
    endereco = json.loads(conteudo)

    return endereco


def cep_valido(cep):
    return True if re.search(r'^(\d{5}-\d{3}|\d{8})$', cep) else False


def main():
    cep = ''

    while cep != 'sair':
        cep = input('CEP: ')

        if cep_valido(cep):
            endereco = consulta(cep)

            if not endereco.get('erro'):
                print('Cidade: %s - %s' % (endereco['localidade'], endereco['uf']) )
                print('Bairro:', endereco['bairro'])
                print('Logradouro:', endereco['logradouro'])
                print('CEP:', endereco['cep'])
                print('\n\n')


if __name__ == '__main__':
    main()