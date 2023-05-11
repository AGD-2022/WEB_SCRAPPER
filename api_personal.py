import requests
import inflection
from bs4 import BeautifulSoup

r = requests.get('https://www.dailysmarty.com/topics/python')

print(r)

datos = BeautifulSoup(r.text, 'html.parser')

print(datos)

#links_all = datos.find_all(['a'])

#print(datos.find_all('a'))

#links_clean = []

#links_clean = links_all['href']

#for link in links_all:
#    if "p" in link:
#        links_clean.append(link)
#        print(f'se agrego '+ link)
#

#print(links_clean)

#post_links = [link for link in links_clean['href'] if link.startswith('/pos')]

#print(inflection.humanize(r.text))

#print(BeautifulSoup(r.text))

#print(BeautifulSoup(inflection.humanize(r.text)))

#print(post_links)

#print(links_clean)
