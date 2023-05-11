import requests
import inflection
from bs4 import BeautifulSoup

r = requests.get('https://www.dailysmarty.com/topics/python')


datos = BeautifulSoup(r.text, 'html.parser')

links_all = datos.find_all(['a'])

post_links = []

for link in links_all:
    href = link.get('href')
    if href and href.startswith('/post'):
        href2 = inflection.titleize(href)
        post_links.append(href2)


links_clean = [item[7:] for item in post_links]

lista_final = links_clean[1:]

for x in lista_final:
    print(x)

print("fin de la ejecucion")
