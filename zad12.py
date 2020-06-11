#-------------------------------------------------------------
# Zadanie 12.
## Napisz program odczytujące dane z
## https://www.otomoto.pl/osobowe/nissan/qashqai/?page=2
## Wyświetl dane o roku i przebiegu aut.

import requests as r
from bs4 import BeautifulSoup

def oferts (address):
    page = r.get(address)
    #print(page)     # sprawdzenie połączenia ze stroną -> gdy odp. jest 200 to jest połączenie
    soup = BeautifulSoup(page.content,'html.parser')
    print(soup.title.text)
    counter = soup.find('span',class_="counter")
    print("="*40)
    print("Wszystkich ofert:",counter.text)
    print("="*40)
    elements = soup.findAll('article',attrs={"class":"adListingItem"})
    print("Ofert na stronie:",len(elements))
    print("="*40)
    for element in elements:
            offertTitle = element.find('h2',class_="offer-title")
            rokProd = element.find('li',attrs ={"data-code":"year"})
            przebieg = element.find('li',attrs ={"data-code":"mileage"})
            print("Pojazd: ",offertTitle.text.strip())
            print("Rok produkcji: ",rokProd.text.strip())
            print("Przebieg: ",przebieg.text.strip())
            print("-"*40)
            
#url = "https://www.otomoto.pl/osobowe/nissan/qashqai/?page=2"

url = input("Podaj adres strony: ")
oferts(url)



# page = r.get(url)
# #print(page)     # sprawdzenie połączenia ze stroną -> gdy odp. jest 200 to jest połączenie
# soup = BeautifulSoup(page.content,'html.parser')
# print(soup.title.text)
# counter = soup.find('span',class_="counter")
# print("="*40)
# print("Wszystkich ofert:",counter.text)
# print("="*40)
# elements = soup.findAll('article',attrs={"class":"adListingItem"})
# print("Ofert na stronie:",len(elements))
# print("="*40)
# for element in elements:
        # offertTitle = element.find('h2',class_="offer-title")
        # rokProd = element.find('li',attrs ={"data-code":"year"})
        # przebieg = element.find('li',attrs ={"data-code":"mileage"})
        # print("Pojazd: ",offertTitle.text.strip())
        # print("Rok produkcji: ",rokProd.text.strip())
        # print("Przebieg: ",przebieg.text.strip())
        # print("-"*40)