import bs4 as bs
import urllib.request
from urllib.error import HTTPError
import re
import time

fim = False
total_cnpj = 10000
total_paginas = 1000
# Condição de parada caso não haja mais páginas para rastrear
while fim == False:
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.3'}
        source = urllib.request.urlopen(
            urllib.request.Request(f"https://b2bleads.com.br/resultado?page={total_paginas}&cnaeSecundario=0&tipoDados=lista",
                                   headers=headers)).read()

        soup = bs.BeautifulSoup(source, features="html.parser")
        all_div = soup.findAll("div", attrs={"class": "d-flex flex-column align-items-end"})

        for div in all_div:
            try:
                li_url = div.a['href']

                cnpj = li_url[-14::]

                # Adiciona a li_url ao arquivo lista_cnpj_coletado
                with open('lista_cnpj_coletado.txt', 'a') as file:
                    file.write(cnpj + '\n')

            except Exception as e:
                print("Não foi possível obter o cnpj:", e)
        print(f"Total CNPJ: {total_cnpj}")
        print(f"Total Páginas: {total_paginas}")
        total_cnpj = total_cnpj + 10
        total_paginas = total_paginas + 1

    #caso não haja url o erro é tratado e o loop é encerrado
    except HTTPError as e:
        print('erro', e)
        fim = True











