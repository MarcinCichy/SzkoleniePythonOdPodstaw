#-------------------------------------------------------------
# Zadanie 1
## Napisz funkcję, która sprawdza czy wyraz jest peselem. Dla uproszczenia
## sprawdzamy czy każdy znak jest cyfrą i czy wyraz ma 11 znaków.
## isPesel(“87122508076”)

# def isPESEL(number):
#     if  len(number) != 11 or not number.isdigit():
#         print("To nie jest właściwy numer PESEL. Podaj jeszcze raz")
#         PESEL = False
#     else:
#         PESEL = True
#     return PESEL

# def isPESEL(numbPESEL):
#     PESEL = True
#     while len(numbPESEL) != 11 or not numbPESEL.isdigit():
#         numbPESEL = input("To nie jest właściwy numer PESEL. Podaj jeszcze raz: \n")
#         PESEL = False
#     return PESEL
    
# numbPESEL = input("Podaj PESEL: \n")
# if isPESEL(numbPESEL): print("To jest właściwy PESEL")

#dla wersji 3.8.2

# import math
# print(math.isqrt(5))

# def is_square(n):
#     return n == math.isqrt(n)*math.isqrt(n)

#-------------------------------------------------------------
# Zadanie 2.
## Napisz funkcję, która stwierdzi czy liczba jest kwadratem liczby całkowitej.


# import math
# def kwadrat(liczba):
#     pierwiastek = round(math.sqrt(liczba),2)
#     print("Pierwiastek z podanej liczby",liczba,"wynosi: ",pierwiastek)
#     is_pierwiastek = True
#     if pierwiastek%1 != 0:                      # jeżeli modulo z dzielenia przez 1 jest różne od zera, to nie jest to liczba całkowita
#            is_pierwiastek = False
#     return is_pierwiastek

# liczba = int(input("Podaj liczbę do spawdzenia: "))
# wynik = kwadrat(liczba)
# print ("Czy podana liczba: ",liczba,", jest kwadratem liczby całkowitej? ->",wynik)

##mozna zrobic odrazu warunek w return (jak u MM) -> return n == math.isqrt(n)*math.isqrt(n) 


#-------------------------------------------------------------
# Zadanie 3.
## Napisz funkcję, która zwraca element środkowy listy.
## middle_element(([1, 2, 3]) = 2 -> 3//2 długośc jest 3 i trzeba zrócić element 1
## middle_element([1, 5, 3, 4]) = 5 -> 4//2-1 długość 4, i trzeba zwrócić eleemt 2

# def middle_element(array):
#     size = len(array)
#     if size%2 == 1:
#         return array[size//2]           # zamiast typować na int mozna dzielic // bez reszty
#     else:
#         return array[size//2-1]


# print(middle_element([1,2,3]))      #wywołanie listy, bez tworzenia nazwy zmiennej
# print(middle_element([1,5,3,4]))


#-------------------------------------------------------------
# Zadanie 4.

# Rozwiąż przykładowe zadanie na serwisie Codility:
## https://app.codility.com/demo/take-sample-test/



# """
# This is a demo task.

# Write a function:

#     def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

#         N is an integer within the range [1..100,000];
#         each element of array A is an integer within the range [−1,000,000..1,000,000].

# """
# def solution (A):
#     list=[]
#     for i in range(0,len(A)):
#         list.append(A[i])
#     list.sort()
#     list.reverse()
#     if min(list) < -1_000_000 or max(list) > 1_000_000:
#         print("List is out of range!!!")
#     else:
#         if max(list) < 0:
#             k=1
#         elif max(list) == 1:
#             k = max(list)+1 
#         else:
#             rangelist = max(list)+1
#             for k in range(1,rangelist+1):
#                 if k not in list:
#                     #return k
#                     break
#         print("The smallest positive integer (greater than 0) that does not occur in A, is:",k,".")
               
#     pass   

# solution(a)

# b=[-145,-258,-654,-55,-2,-548,-3,-555,-255]
# c=[-145,-258,-654,-55,-2,-548,-3,-555,-255,1]
# d=[1_000_001,50,-3,56,23,-2,3,9,55,-23,67,12,-11,345,1,0,2,4,5,6,7,8,10,11,12,13,14]
# e=[-48752,50,-3,56,7,23,15,-2,3,9,55,-23,67,12,0,-11,345,2,5,6,4,8,10,12,1,13,14]
# f=[1,2,57,9,45,7,23,8,962,4,5,3]
# g=[1, 3, 6, 4, 1, 2]
# h=[1, 2, 3]
# i=[-1,-3]

## a = [b,c,d,e,f,g,h,i]
## for i range(0,i)
## solution(a)

## CodingBat.com/python -> zadania -> codingbat.com/python
## codility lessons -> app.codility.com/programmers/lessons/1-iterations


#---------------  rozwiązanie MM na 66%
# def solution(A):
#     for i in range(1,len(A)+2):
#         if not i in A:
#             return i


# #---------------  rozwiązanie MM na 88%
# def solution(A):
#     A = [x for x in A if x >0]
#     A = sorted(A)
#     if 1 not in A:
#         return 1
#     for i in range(1,len(A)):
#         if A[i] ==A[i-1]:
#             continue
#         if A[i] ==A[i-1]+1:
#             continue    
#         return A[i-1]+1 
#     return len(A)+1     


#---------------  rozwiązanie MM na 100%
#a=set(A) -> szybciej robi operacje niz lista

# def solution ( A ):
#     # write your code in Python 3.6
#     s = set (A)
#     for i in range ( 1 , len (A)+ 2 ):
#         if not i in s:
#            return i 

#-------------------------------------------------------------
# Zadanie 5.
## Napisz funkcję, która jako argument przyjmuje listę i zwraca element, który
## występuje najczęściej.

# def max_appearence(table):
#     dictionary ={}                              # przyjmuje pusty słownik, aby móc go uzupełnić zliczonymi wystąpieniami danego elementu
#     dict2 = {}                                  # przyjmuje pusty słownik, aby wypełnic go maksymalnymi wartosciami
#     for i in table:                             # zlicza wystąpienia wszystkich elementów w tabeli
#         table.count(i)      
#         dictionary[i]=table.count(i)            # wypełnia słownik elementem i ilościa jego wystąpień (keys=i, value = table.count(i))
#     # print(dictionary)
#     maximum = max(dictionary.values())          # ustanawia maksymalną wartość wystęującą w słowniku, w wartosciach (nie w kluczach)   
#    #  print(maximum)
#     for keys,values in dictionary.items():      # iteruje po wszystkich elemmentach słownika  (klucz, wartość)
#         if values == maximum:                   # jeżeli wartość jest równa maksimum
#             dict2[keys]=values                  # to wpisuje do słownika dict2 tą wartość wraz z kluczem(elementem sprawdzanym)
#     return dict2
#     # return print(dict2)
#     #return print("Element:",dict2.keys(),"występuje",dict2.values(),"razy.")

# array = ['e','f','g','j','d','e','j','k','h','f','d','m','n','b','f','r','f','f','f','f']
# array =[1,4,6,457,8,8,6,8,3,7,8,0,8,8,8,8,5,4,3,3,3,5,6,6,8,9,0,6,3,3,5,7]
# array = ["f","g","e","c","a","s","r","d","v","c","d","e","f","k","r"]
# print(max_appearence(array))

#-------------------------------------------------------------
# Zadanie 6.
## Napisz funkcję, która jako argument przyjmuje listę Stringów. Jako wynik ma
## zwracać listę wszystkich słów, które zawierają słowa 5-literowe.

# def onlyFiveLetter(words):
#     scoreList=[]
#     for i in range(len(words)):
#         if len(words[i]) == 5:
#             scoreList.append(words[i])
#     return scoreList



# listaSlow = ["dom", "lalka","kot","domek","kajak","histo","12345"]
# print(onlyFiveLetter(listaSlow))


#-------------------------------------------------------------
#Zadanie 7
## Napisz funkcję, która jako argument przyjmuje datę, a jako wartość zwraca kurs
## złota. Wykorzystaj API NBP:


# import requests as r
# # dostajemy stronę internetową
# response = r.get('https://api.nbp.pl/api/cenyzlota/2020-05-19?format=json')
# json = response.json()
# gold = json[0]  #od zera bo json to list, która ma jeden element na pozycjo 0
# print((type(gold)))
# print(type(json))
# print("Cena złota, to",gold['cena'],'zł')


#-------------------------------------------------------------
#Zadanie 8
## Napisz funkcje, która jako argument przyjmuje datę, a jako wartość zwraca kurs
## dolara. Wykorzystaj API NBP:
## https://api.nbp.pl/api/exchangerates/rates/c/usd/2020-05-19?format=json

# import requests as r

# response = r. get("https://api.nbp.pl/api/exchangerates/rates/c/usd/2020-05-19?format=json")
# json = response.json()
# print(json)
# print(type(json))
# print(json['rates'][0]["bid"])



#-------------------------------------------------------------
# Zadanie 9.
## Napisz program, który pobiera dane z serwisu kaggle.com happinnes.csv i
## pokazuje kraj, w którym ludzie są najbardziej i najmniej szczęśliwi.

# import pandas as pd

# df = pd.read_csv("E://Programowanie//Python//KURS//2019.csv")        #df->data frame
# #print(df.head())        #wyświetla pierwsze dane
# #print(df.columns)
# #print(df.index)        # index to pierwszy element po którym dane sa posegregowane

# #print(type(df))
# max_index = 0       #indeks z elementem maksymalnym
# min_index = 0       #indeks z elementem minimalnym
# for index in df.index:
#     #print(index)
#     if (df["Score"][index]>df["Score"][max_index]):
#         max_index = index
#     if (df["Score"][index]<df["Score"][min_index]):
#         min_index = index

# print(df["Country or region"][max_index],df["Score"][max_index])
# print(df["Country or region"][min_index],df["Score"][min_index])
#    # print(df["Score"][index])   #dla każdego indeksu


#-------------------------------------------------------------
# Zadanie 10.
## Napisz funkcję, która sumuje wszystkie liczby parzyste listy.

# def solution(A):
#     sum = 0
#     for value in A:
#         if value%2 == 0:
#             sum+=value
#     return sum

# print(solution([-6,-91,1011,-100,84,-22,0,1,473]))


#-------------------------------------------------------------
# Zadanie 11.  --> do zabawy
## Napisz program, który pobiera z api: https://openweathermap.org/api aktualną
# ## pogodę.
# import requests as r

# url = "http://api.openweathermap.org/data/2.5/weather?q=Siemianowice Śląskie&appid=98a4fd3b5835c984c381855e492c7527"
# #url = "http://api.openweathermap.org/data/2.5/weather?id=3086024&appid=98a4fd3b5835c984c381855e492c7527"
# response = r.get(url)
# print(response)
# json = response.json()
# dictionary = response.json()
# print(dictionary)
# temperature = dictionary['main']['temp']
# weather = dictionary['clouds']['all']
# print('Temperatura w Siemianowicach Śląskich wynosi: ',str(round((temperature-273.5),2))+ '\u00B0C')
# print('W Siemianowicach Śląskich jest teraz:', weather)
# ## w Kelwinach  print('Temperatura w Siemianowicach Śląskich wynosi: ',(str(temperature) + '\u00B0K'))


#-------------------------------------------------------------
# Zadanie 12.
## Napisz program odczytujące dane z
## https://www.otomoto.pl/osobowe/nissan/qashqai/?page=2
## Wyświetl dane o roku i przebiegu aut.


import requests as r
from bs4 import BeautifulSoup

def offerts (address):
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
offerts(url)

