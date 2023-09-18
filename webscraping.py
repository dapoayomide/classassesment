from bs4 import BeautifulSoup
import requests

response = requests.get('https://goku.sx/home/')

contents = BeautifulSoup(response.text, features='html.parser')

container = contents.find('div', id ='trending-movies')

items = container.find_all('div' , class_='item')

for names in items:
    name = names.find('h3')
    print(name.text)
    info = names.find('div' , class_='info-split').find_all('div')

    year = info[0]
    print(year.text)
    time =info[2]
    print(time.text)

    
