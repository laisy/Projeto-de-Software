# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import string
import re
import unicodedata

class Web_Scraping:

  def salvarDados(info, biografia):
    with open(f'{biografia}.txt', 'w') as file:
      file.write(f'{info}')


  def ler(biografia):
    with open(f'{biografia}', 'r') as fr:
       
        # ler linha por linha
        lines = fr.readlines()
        
        ptr = 1 #sentila
      
        # abre o aquivo em modo de leitura
        with open(f'{biografia}', 'w') as fw:
            for line in lines:
                
                # remover as linhas com \n e linhas do inicio e final que tem js
                if ptr > 16 and ptr < (len(lines)-7) and line != "\n":
                    fw.write(line)
                ptr += 1
                
  #pede o que está no site por meio da url
  def fazerRequest(url):
    resposta = requests.get(url)
    texto = BeautifulSoup(resposta.text, 'html.parser')
    return texto

  #Pega as informações no formato de texto da pagina
  def pegarInfo(texto):
      arrayText = [x.extract().getText() for x in texto.findAll('p')]
      textoFinal = ""

      def isEnglish(s):
          return s.translate(string.punctuation).isalnum()

      for linha in arrayText:
          for letra in linha:
            if (letra != " "):
                if (isEnglish(letra) or letra == "\n"):
                    textoFinal += str(re.sub('[^a-zA-ZáéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇõ]',' ', letra))
                else:
                    textoFinal += " "
            else:
                textoFinal += " "

      return textoFinal

  def processar (url):

      web = Web_Scraping
      pegando = web.fazerRequest(url)
      info = str(web.pegarInfo(pegando))

      return info
