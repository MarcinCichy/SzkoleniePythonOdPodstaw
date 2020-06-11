#-------------------------------------------------------------
# Zadanie 1.

## Chcemy wybrać najlepsze liceum dla Jacka. Jacek ma 180 punktów
## rekrutacyjnych i może pójść do szkoły, która będzie
## oddalona maksymalnie o 10 km od jego domu. W tym celu, stwórz klase
## HighSchool , która będzie zawierała nazwę,
## próg punktowy oraz odległość liceum od Jacka w kilometrach. Następnie
## w metodzie stwórz listę liceów typu list i wypisz informacje o każdym z
## nich, używając pętli.
## Dopasuj najlepsze liceum, do którego może pójść Jacek. W przypadku, gdy
## w liście nie znajduje się liceum, do którego Jacek może aplikować, wypisz
## stosowny komunikat. Przykładowy output:
## LO im. Jana Zamoyskiego needs 173 pts and is 15 km away.
## LO im. Mikołaja Kopernika needs 193 pts and is 7 km away.
## LO im. Batalionu "Zoska" needs 122 pts and is 6 km away.
#3 Apply for LO im. Batalionu "Zoska".


# klasa to definicja dla obiektów. W Pythonie plik nie musi się nazywac tak samo jak klasa(a w Javie musi)
# klasa to nowy typ (jak string, int, list itd)

# class HighSchool :

#     #funkcja, metoda -> tego typu, to konstruktor
#     def __init__ ( self , name , distance , points ):
#         self .name =name
#         self .distance = distance
#         self .points = points
# schools = []
# # LO im. Jana Zamoyskiego needs 173 pts and is 15 km away.
# # LO im. Mikołaja Kopernika needs 193 pts and is 7 km away.
# # LO im. Batalionu "Zoska" needs 122 pts and is 6 km away.

# # do listy można dodawac obiekty, tak jak dodawało sie zmienne, string, int itd
# # dzieki temu zapisowi(jak nizej) trudniej jest popełnic bład, tak samo robi się w funkcjach, przypisanie zmiennych do konkretnych argumentow w definicji klasy
# schools.append(HighSchool( name = 'LO im. Jana Zamoyskiego' , distance = 15 , points = 173 ))
# schools.append(HighSchool( name = 'LO Mikolaja Kopernika' , distance = 7 , points = 193 ))
# schools.append(HighSchool( 'Zoska' , 6 ,  122 ))  #można tez tak wywołac metody
# number_of_pooints = 180     #ilość punktów Jacka
# distance = 10               #maksymalny dozwolony dystans do szkoły
# max_school = None           #pusta wartość, zakładamy na początku, że szkoły nie mamy. None to słowo kluczowe, ni emożna go zadeklarowac. Jest to nazwa Pythona
# for school in schools:      #sprawdzamy, czy szkoła spełnia warunki
#     if school.points<=number_of_pooints and school.distance<=distance:      #ilośc punktów i odległosc musza byc mniejsze równe od tych od Jacka
#         if max_school:              # jeżeli max_school jest None, to pomijamy p rzechodzimy do elsa. (if max_school !=None), 
#             if school.points>max_school.points:
#                 max_school = school
#         else:
#             max_school = school
# if max_school:
#     print (max_school.name)
# else :
#     print ( 'Nie znaleziono szkoly' )


# ###################
# name =None
# if name:            #czy name nie jest puste, jezeli jest puste, to przechodzi do else
#     print('TAK')
# else:
#     print('NIE')

# #będzie NIE, bo zmienne name jest None


#-------------------------------------------------------------
# Zadanie 2.
## Stwórz klasę Book , która będzie zawierała informacje o tytule, autorze, liczbie stron oraz dacie wydrukowania książki. 
## Ponadto, klasa ma zawierać metodę get_days() , która zwraca wiek książki w dniach (obchodzi nas przedział czasowy od wydrukowania książki do dziś). 
## Następnie w metodzie utwórz liste ksiazek i wypisz informacje o każdej z nich oraz jej wiek w dniach. Wpisz tytuł najstarszej
## z nich (w przypadku kilku najstarszych, wypisz dowolna). 
## Przykładowy output:
## 1. book "Data science od podstaw. Analiza danych w Pythonie" is 142 days old.
## 2. book "HTML i CSS. Zaprojektuj i zbuduj witryne WWW." is 536 days old.
# ## 3. book "MATEMATYKA ZADANIA MATURALNE I EGZAMINACYJNE" is 9080 days old.
# ## The oldest book is "MATEMATYKA ZADANIA MATURALNE I EGZAMINACYJNE”.

import datetime as d


class Book:
    def __init__(self, title, author,date):
        self.title= title
        self.author = author
        self.date = date

    # wywoływane, gdy wpiszemy print(book)
    def __repr__(self):
        return self.title+', '+str(self.get_days())   #tu podajemy, co chcemy wyswietlic printem

    def get_days(self):
        #biezące data d.date.today()
        return (d.date.today()-self.date).days  #days -> ilość dni

example_date = d.date(2020,2,2)
#print(example_date)

books = []

books.append(Book("programowanie Python","Jan Nowak",example_date))     #gdy wywołujem Book, to wywoływana jest metoda __init__
books.append(Book("HTML i CSS ZAprojektuj stronę","Zdzisław Kowalski",d.date(2020,5,20)))

for book in books:
    print(book)     #tu wywyoływana jest metoda repr

#-------------------------------------------------------------
# Zadanie 3.
# Stwórzmy szkielet dokumentu w HTML5.
