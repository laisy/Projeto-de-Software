import requests
from bs4 import BeautifulSoup
import re

class Web_Scraping:

    def salvarDados(info, biografia):
        with open(f'{biografia}.txt', 'w', encoding="utf-8") as file:
            file.write(f'{info}')

    def ler(biografia):
        with open(f'{biografia}', 'r', encoding="utf-8") as fr:

            # ler linha por linha
            lines = fr.readlines()

            ptr = 1  # sentila

            # abre o aquivo em modo de leitura
            with open(f'{biografia}', 'w', encoding="utf-8") as fw:
                for line in lines:

                    # remover as linhas com \n e linhas do inicio e final que tem js
                    if ptr > 16 and (ptr < (len(lines) - 7) ) and line != "\n" :
                         newLine = re.sub('[^a-zA-ZáéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇō: \n ]',' ', line)
                         fw.write(newLine)
                    ptr += 1

    # pede o que está no site por meio da url
    def fazerRequest(url):
        resposta = requests.get(url)
        texto = BeautifulSoup(resposta.text, 'html.parser')
        return texto

    # Pega as informações no formato de texto da pagina
    def pegarInfo(texto):
        info = texto.find('main', {'class': 'mw-body'}).get_text()
        return info


def main():
    nome_arquivo = 'pegando_texto_do_wiki'
    url = 'https://pt.wikipedia.org/wiki/Biologia'

    web = Web_Scraping
    pegando = web.fazerRequest(url)
    info = web.pegarInfo(pegando)
    web.salvarDados(info, nome_arquivo)
    web.ler(f'{nome_arquivo}.txt')


if __name__ == '__main__':
    main()