#-------------------------------------------------------------
# Zadanie 1
##  Napisz program, który odczytuje n i wypisuje sumę liczb od 1 do n.

# liczba = int(input("Podaj liczbę: \n"))
# suma=0
# for i in range(1,liczba+1):
#        #print (i)
#        suma += i
#        print(i,suma)
# print("Suma liczb, to:",suma)


#-------------------------------------------------------------
# Zadanie 2
## Napisz program który wygeneruje za pomocą print (wielkość wieżyczki podaje
## użytkownik)
## *
## **
## ***

# wysWie = int(input("Podaj wysokość wieżyczki: "))
# for i in range(1,wysWie+1):
#     print(i*"*")


#-------------------------------------------------------------
# Zadanie 3
## Napisz program, który wypisuje co trzecią literę imienia.

# imie = input("Podaj imię: ")
# dlImie = len(imie)
# print("---- pierwszy sposób -----")
# for i in range(2,dlImie,3):
#     print(imie[i])
# print("---- drugi sposób -----")
# imie = input ( 'Podaj imie \n ' )
# for index,value in enumerate (imie):
#     if index% 3 == 2 :
#         print (value)


#-------------------------------------------------------------
# Zadanie 4
## Napisz program, który odczytuje liczbę i wypisuje liczbę dzielników danej liczby.

# liczba = int(input("Podaj liczbę: "))
# ilDzielniki = 0
# for i in range(1,liczba+1):
#     if liczba%i == 0:
#         ilDzielniki += 1
#         print (i, end=" ")

# print("\nLiczba dzielników liczby:",liczba,",to: ",ilDzielniki)


#-------------------------------------------------------------
# Zadanie 5
## Odczytaj wyraz i wypisz wszystkie znaki w wyrazie w oddzielnej linii.

# imie = input("Podaj imię: ")
# ##----- sposób 1 --------
# print("-----------------1---------------")
# for i in range(0,(len(imie))):
#     print(imie[i])

# ##----- sposób 2 --------
# print("-----------------2---------------")
# for i in imie:
#     print(i)

# ##----- sposób 3--------
# print("-----------------3---------------")
# name = imie
# i = 1
# length = len(name) 
# for i in range(0,length):
#     value = name[i]
#     print(name[i])


# ##----- sposób 4--------
# print("-----------------4---------------")
# for i,value in enumerate(name):
#     print(value)


#-------------------------------------------------------------
# Zadanie 6
## Napisz program, który odczytuje kod pocztowy i sprawdza czy kod pocztowy jest poprawny.

# kodPocztowy = input("Podaj kod pocztowy w formacie XX-XXX: ")
# czToKodPocztowy = True

# if len(kodPocztowy) == 6 and kodPocztowy[2] == "-":
#     for i in range(0,6):
#         if i == 2:
#             continue
#         if not kodPocztowy[i].isdigit():
#             czToKodPocztowy = False
# else:
#     czToKodPocztowy = False
# if czToKodPocztowy:
#     print("Kod jest poprawny")
# else:
#     print("Kod jest błędny")


#-------------------------------------------------------------
# Zadanie 7
## Napisz program, który wypisuje liczby od 100 do 50, w tej kolejności.

# for i in range(100,49,-1):
#     print(i)

#-------------------------------------------------------------
# Zadanie 8

# import turtle
# win = turtle.Screen() # pojawia sie okno
# circle = turtle.Turtle() # będziemy mieli zmienną na ktorej mozemy rysowac 

# for i in range(1,361):  
#     circle.hideturtle() 
    
#     circle.left(1)
#     circle.forward(3)
   

# win.mainloop()

#-------------------------------------------------------------
# Zadadnie 9
## Co z tym kodem jest nie tak?
# for i in range(1,50):
# print(i)
#brak wcięcia


#-------------------------------------------------------------
# Zadadanie 10

# import math as m
# r = float(input("Podaj promień koła :\n"))
# print ("Pole koła wynosi:",round((m.pi*r**2),2))


#-------------------------------------------------------------
# Zadanie 11
## Napisz program, który wypisuje liczby od 100 do 50 (w tej kolejności).

# for i in range(100,49,-1):
#     print(i)


#-------------------------------------------------------------
# Zadanie 12
## Jaki będzie wynik programu:

# for i in range ( 1 , 50 ):
#     print (i)
#     if i== 15:
#         break
# print ( 'Koniec' )  

## Gdy osiągnie 15, to przerwie działanie pętli

#-------------------------------------------------------------
# Zadadnie 13
## Jaki będzie wynik programu:

# for i in range ( 1 , 50 ):
#     if i== 15 :
#         continue #powraca do początku pętli, ale nie zrobił print(i) dla 15 !!!
#     print (i)


#-------------------------------------------------------------
# Zadanie 14
## Napisz program, który tworzy 25 plików na dysku o nazwach:
## 1.py
## 2.py
## 3.py
## ….
## 25.py


# for i in range(1,26):
#     print(str(i)+".py")     #zamiana cyfry na string
#     name = str(i)+'.py'
#     file = open(name,"w")
#     file.close()

## E:\Programowanie\Python\KURS\folder

#-------------------------------------------------------------
# Zadanie 15
## Napisz program, który wypisuje wszystkie liczby od 2 do 1000, które mają 3 cyfry.

# for i in range(2,1001):
#     if len(str(i)) == 3:
#         print (i)

#-------------------------------------------------------------
#  cwiczenie 16
## Napisz program, który odczytuje z
## https://pogoda.onet.pl/prognoza-pogody/warszawa-357732 l pogodę w Warszawie.
## crawling, scraping 

#https://pogoda.onet.pl/prognoza-pogody/siemianowice-slaskie-344101

# import requests as r
# url = 'https://pogoda.onet.pl/prognoza-pogody/siemianowice-slaskie-344101'
# response = r.get(url)
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(response.content,'html.parser')
# print(soup.title.text)
# #element = soup.find('span',class_="feelTempValue")
# element = soup.find('div',class_="temp")
# print('Temperatura w Siemianowice to: ',element.text)

#-------------------------------------------------------------
# Zadanie 17
## Napisz program, który losuje 5 liczb z zakresu od 2 do 50.

# import random as r

# for i in range (1,6):
#     print(r.randrange(2,51))

#-------------------------------------------------------------
# Zadanie 18
## Napisz program, który wypisuje co drugą literę imienia.


# name = input ( 'Podaj imie \n ' )
# # ----- sposób 1 -----
# print("----- sposób 1 -----")
# for i,value in enumerate (name):
#     if i% 2 == 1 :
#         print (value, end=" ")

# # ----- sposób 2 -----
# print("\n----- sposób 2 -----")
# # imie = input("Podaj imię: ")
# imie = name
# for i in range(1,(len(imie)),2):
#     print(imie[i], end=" ")

#-------------------------------------------------------------
# Zadanie 19
## Napisz program, który wypisuje liczby od 5 do 100, które mają dokładnie 4 dzielniki.

# for i in range ( 5 , 101 ):
#     score = 0
#     for j in range ( 1 ,i+ 1 ):
#         if i %j == 0 :
#             score += 1
#     if score == 4 :
#         print (i)


#-------------------------------------------------------------
# Zadanie 20
## Napisz program, który wypisuje liczby od 10 do 500, oprócz 3, 5, 100, 150. Użyj continue.

# for i in range(10,501):
#     if i == 100 or i == 150:  #bez i == 3 or i == 5 - bo zakres pętli jest od 10
#         continue
#     print(i)


#-------------------------------------------------------------
# Zadanie 21
## Napisz program rysujący w konsoli literę L:
## *
## *
## *
## *
## *
## *
## *****

# for i in range(1,7):
#     print("*")
# print(5*"*")



#-------------------------------------------------------------
# Zadanie 22
## Napisz program, który pokazuje kalendarz z roku 2015.

# import calendar as c
# print(c.calendar(2015))


#-------------------------------------------------------------
# Zadanie 23
## Napisz program, który pokazuje losowe przysłowia. Przysłów możemy
## mieć maksymalnie 6.

# import random as r
# quotes = [ "Przyslowie 1" , "Przyslowie 2" , "Przyslowie 3" , "Przyslowie 4" , "Przyslowie 5" , "Przyslowie 6" ]
# print (quotes[r.randrange( 0 , len (quotes))],"\n") #wyświetla losowo pozycję z listy od pozycji 0 do pozycji określonej długoscia listy -> len(quotes+1) <- bo trzeba domknąć przedział


#-------------------------------------------------------------
# Zadanie 24 -- sprawdzić!!!!!!
## Napisz program, który odczytuje liczbę n i na ekran wypisuje
## 2*n!+2*(n-2)!. Gdzie ! oznacza silnie.


# n = int ( input ("Podaj liczbę n: " ))
# silnia1 = 1
# silnia2 = 1
# for i in range (1 ,n+1):
#     silnia1 *=i
#     if i == n-2:
#         silnia2 = silnia1
# print(2*(silnia2+silnia1))

#-------------------------------------------------------------
# Zadanie 25 -- sprawdzić!!!!!!
## Napisz program, który sprawdza czy wyraz jest palindromem przy użyciu pętli while.

# ----- sposób 1 -----
# print("----- sposób 1 -----")
# word = input ( 'Podaj slowo \n ' )
# is_palindrom = True                 #zmienna pomocnicza przyjmuje wartość TRUE
# left = 0                            #ustalamy początkową wartość zmiennej left na 0, aby móc odczytac pierwszą(zerową) literę ciągu
# right = len (word)- 1               #zmienna right przyjmuje wartość odpowiadającą numerowi ostatniej litery ciagu (-1, bo liczymy od zera)
# print(word[left])
# print(word[right])
# while left!=right:                  # do chwili gdy pierwsza i ostatnia ( a następnie kolejne druga i przedostatnia itd.) litera ciągu sa takie same wykonuj pętle while, zakończ gdy będą różne 
#     if word[left]!=word[right]:     # sprawdź czy pierwsza i ostatnia litera (i odpowiednio kolejne) są różne
#         is_palindrom = False        # jeżeli tak, to przypiz zmiennej is_palindrom wartość False
#         break                       # i zakończ pętlę
#     left+= 1                        # zmień wartość zmiennej left o 1 - aby sprawdzic następną literę ciągu(od lewej)
#     right-= 1                       # zmień wartość zmiennej right o -1 (w dół) - aby sprawdzic następną literę ciągu(od prawej) i porównać je w pętli while i w ifie
#     print(word[left],"- z lewej")
#     print(word[right],"- z prawej")

# print (is_palindrom)                # wyświetl wartość zmiennej is_palindrom na ekranie w zaleznosci jaka otrzymala ona wartoś


# # ----- sposób 2 -----
# print("----- sposób 2 -----")
# #word = input ( 'Podaj wyraz \n ' )
# left = 0
# right = len (word)- 1
# is_palindrom = True
# while left<right:
#     if word[left]<word[right]:
#         is_palindrom = False
#         break
#     left+= 1
#     right-= 1


# print (is_palindrom)   
# if is_palindrom:
#     print ( 'Palindrom' )
# else :
#     print ( 'To nie jest palindrom' )




#-------------------------------------------------------------
# Zadanie 26 
## Napisz program, który odczytuje liczbę n i na ekran wypisuje n- ty
## wyraz ciągu
## x(0) = 5
## x(n) = x(n-1)+2(x(n-2)


# Niepoprawna treść.