#-------------------------------------------------------------
# Zadanie 1
## Napisz program, który pobiera dane z serwisu kaggle.com happinnes.csv i
# ## pokazuje kraj, w którym ludzie są najbardziej i najmniej szczęśliwi.
# import pandas as pd

# df = pd.read_csv("E://Programowanie//Python//KURS//2019.csv")        #df->data frame
# #print(df.head())        #wyświetla pierwsze dane
# #print(df.columns)

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
# Zadanie 2

# def solution(A):
#     sum = 0
#     for value in A:
#         if value%2 == 0:
#             #sum+=value -> to lepszy zapis
#             sum = (sum+value)
#     return sum

# print(solution([-6,-91,1011,-100,84,-22,0,1,473]))


# def solution (A):
#     suma =0
#     for value in A:
#         if value%2 == 0:
#             #suma = suma + value
#             suma += value
#     return suma

# print(solution([-6,-91,1011,-100,84,-22,0,1,473]))


#-------------------------------------------------------------
# Zadanie 3
## Stwórz klasę osoba, która będzie zawierała następujące dane:
## - imię
## - nazwisko
## - pesel

#Klasa = definicja obiektu

#Dane o pokojach i dostępnościach dla sal szkoleniowych
#Użytkownicy którzy beda sie rejestrowac email i haslem

#definicja
# #Klasa to nowy typ
# class Person:
#                        # funkcje w programowaniu obiektowym nazywamy metodą
#                         #  __ cos specjalnego
#                         #specjalna metoda o nazwie __init__
#                         #self to konstruktor, specjalna metoda, która tworzy obiekt
#     def __init__(self,name, surname, pesel):
#         #moje imie = imie, które pochodzi z argumentu funkcji
#         self.name = name
#         self.surname = surname
#         self.pesel = pesel
# # konkretny element klasy, to jest obiekt

# p = Person("Adma","Kowalski","1234567890")
# print(p.name,p.surname)
# p2 = Person("Jan","Nowak","98745632102") #-> nazwa zmiennej tu p2 moze byc dowolna
# print(p2.name,p2.surname,p2.pesel)

#-------------------------------------------------------------
# Zadanie 4.
## Stwórz klasę Mem, która przechowuje informację o obrazkach:
## - nazwa
## - url obrazka
## - czy jest ulubiony
## Url obrazka musi być poprawnym adresem url. Stwórz przykładową listę
## Memów.
## Wyświetl tylko te memy, które są ulubione.

# class Mem:
#     # jeżeli is_favorite nie zostanie podane, to ustaw domyślnie wartość False
#     #if dla definicji metod, to domyslny typ
#     # konstrutor
#     def __init__(self,name,url,is_favorite=False):
#         self.name = name
#         self.url = url
#         self.is_favorite = is_favorite

# # obiektem jest m i m2
# m = Mem("programowanie jest super","http://super.jpg")  #is_favorite = False domyslnie
# m2 = Mem("Jestem Bogiem","http://aa.jpg",True)      #is_favorite = True
# #print(m.name,m.is_favorite)
# #print(m2.name,m2.is_favorite)


# mems = [m,m2]  # z obiektów m i m2 można zrobic listę, tutaj mems
# mems.append(Mem("Python jest swietny","http://python5.jpg",True))

# for mem in mems:
#     if not mem.is_favorite:
#         print(mem.name,mem.url)


#-------------------------------------------------------------
# Zadanie 5.
## Stwórz klasę Zapytanie, która przechowuje zapytania od użytkowników strony internetowej.
## Będziemy przechowywać następujące informację:
## - kto stworzył zapytanie (nazwa użytkownika)
## - data stworzenia zapytania
## Stwórz metodę, która sprawdza czy zapytanie jest starsze niż 2 tygodnie.

# import datetime
# from dateutil.relativedelta import relativedelta
# class Inquiry :
#     def __init__ ( self , username , date ):
#         self .username = username
#         self .date = date
#     def __repr__ ( self ):
#         return self .username+ ' ' + self .date
#     def is_old ( self ):
#         result = self .date+relativedelta( days = 14 )
#         return (result< datetime.date.today())
# dt = datetime.date( 2020 , 2 , 2 )
# dt2 = datetime.date( 2020 , 5 , 20 )
# i = Inquiry( 'michalos' ,dt)
# i2 = Inquiry( 'anna' ,dt2)
# print (i.is_old())
# print (i2.is_old())

#-------------------------------------------------------------
# Zadanie 6.
## Stwórz klasę Apartment , która będzie zawierała informacje o mieście, w
## którym się znajduje, powierzchni w metrach
## kwadratowych, oraz cenie za metr mieszkania. Ponadto, klasa ma zawierać
## metodę get_full_price() , która
## zwraca cenę za mieszkanie przemnożona przez 0.95 (rabat od dewelopera).
## Wyznacz średnią cenę mieszkań. Uwaga: wszystkie wartości liczbowe w
## tym zadaniu wypisz, zaokrąglając do dwóch
## miejsc po przecinku.
## Przykładowy output:
## 1. Apartment in Warsaw costs 771875.00.
## 2. Apartment in Cracow costs 779000.00.
## 3. Apartment in Gdansk costs 855000.00.
## Mean price is 801958.31


# class Apartment:
#         #dict to dictionary, jako argument funkcji/metody
#         #jakie dane są nam potrzebne, metoda ktora jest wywolywana przy zapise Apartment()
#         #tworzone jest miejsce w pamięci
#     def __init__(self, dict):
#         self.city = dict['city'] #wartosc słownika przypisywana jest do self.city ja miasto
#         self.price_per_meter = dict['price_per_meter']
#         self.area = dict['area']
#     #definicja metody full_price
#     def full_price(self):
#         return round(self.area*self.price_per_meter*0.95,2)
    
#     def print_description(self):
#         print(self.city,self.full_price(),"tyś złotych")

#     def __repr__(self):
#         return self.city+' '+str(self.full_price())

# apartment = Apartment({'city': 'Warszawa','price_per_meter': 10,'area': 50.29})
# print("Repr wywoływane",apartment)
# print(apartment)
# full = apartment.full_price()
# print(full)

# # print(apartment.city)
# # print(apartment.full_price())
# apartment.print_description()

# apartment2 = Apartment({'city': 'Kraków','price_per_meter': 8,'area': 79.00})
# apartment2.print_description()



#-------------------------------------------------------------
# Zadanie 7.

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



class HighSchool :
    def __init__ ( self , name , distance , points ):
        self .name =name
        self .distance = distance
        self .points = points
schools = []
# LO im. Jana Zamoyskiego needs 173 pts and is 15 km away.
# LO im. Mikołaja Kopernika needs 193 pts and is 7 km away.
# LO im. Batalionu "Zoska" needs 122 pts and is 6 km away.
schools.append(HighSchool( name = 'LO im. Jana Zamoyskiego' , distance = 15 , points = 173 ))
schools.append(HighSchool( name = 'LO Mikolaja Kopernika' , distance = 7 , points = 193 ))
schools.append(HighSchool( name = 'Zoska' , distance = 6 , points = 122 ))
number_of_pooints = 180
distance = 10
max_school = None
for school in schools:
    if school.points<=number_of_pooints and school.distance<=distance:
        if max_school:
            if school.points>max_school.points:
                max_school = school
        else :
            max_school = school
if max_school:
    print (max_school.name)
else :
    print ( 'Nie znaleziono szkoly' )

#-------------------------------------------------------------
# Zadanie 8.