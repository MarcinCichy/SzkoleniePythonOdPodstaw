#-------------------------------------------------------------
# Zadanie 1
## Napisz program, który odczytuje 2 liczby i wypisuje na ekran największą z liczb.


# liczba1 = int(input("Podaj liczbe A: \n"))
# liczba2 = int(input("Podaj liczbe B: \n"))
# if liczba1 > liczba2:
#     print ("Wiekszą jest liczba A=",liczba1)
# else:
#     print ("Wiekszą jest liczba B=",liczba2)

#-------------------------------------------------------------
# Zadanie 2
## Napisz program, który odczytuje 3 liczby i wypisuje na ekran największą z liczb.

# liczba1 = int(input("Podaj liczbe A: \n"))
# liczba2 = int(input("Podaj liczbe B: \n"))
# liczba3 = int(input("Podaj liczbe C: \n"))
# if liczba1 == liczba2 or liczba1 == liczba3 or liczba2 == liczba3:
#     print("Conajmniej 2 liczby są równe")
# elif liczba1 > liczba2 and liczba1 > liczba3:
#     print ("Najwiekszą jest liczba A=",liczba1)
# elif liczba2 > liczba1 and liczba2 > liczba3:
#     print ("Najwiekszą jest liczba B=",liczba2)
# else:
#     print ("Najwiekszą jest liczba C=",liczba3)

# --------- inna wersja -----------
# a = int(input('Podaj liczbę 1\n'))
# b = int(input('Podaj liczbę 2\n'))
# c = int(input('Podaj liczbę 3\n'))
# if a>b:
#     max = a  # a jest kandydatem na maksa
# else:
#     max = b # b jest kandydatem na maksa
# if c>max:
#     max = c
# print(max)

#-------------------------------------------------------------
# Zadanie 3
## Napisz program, który sprawdza czy wprowadzony wyraz jest palindromem.

# wyraz = input("Podaj wyraz: \n")
# # print (wyraz[::-1])
# wyrazOdwr = wyraz[::-1]
# print("Wyraz odwrócony:",wyrazOdwr)
# if wyraz == wyrazOdwr:
#     print("TAK - wyraz jest palindromem")
# else:
#     print("NIE - wyraz nie jest palindromem")


#-------------------------------------------------------------
# Zadanie 4
## Napisz program, który odczytuje 2 zmienne zapisuje je do zmiennej a i b
## następnie zamienia wartości zmiennych.
## a = 5
## b = 10
## print(a,b) # przed zamianą 5, 10
## # zamiana
## print(a,b) # po zamianie zmiennych

# liczbaA = int(input("Podaj liczbe A: \n"))
# liczbaB = int(input("Podaj liczbe B: \n"))
# print ("Liczba A =",liczbaA,", liczba B =",liczbaB)
# liczba_temp=liczbaA
# liczbaA=liczbaB
# liczbaB=liczba_temp

# print ("Liczba A =",liczbaA,", liczba B =",liczbaB)

#-------------------------------------------------------------
# Zadanie 5
## Napisz program, który odczytuje zdanie i wypisuje litery od 2 do 4.
## Przykładowo:
## Polska to piękny kraj
## Powinno wypisać:
## ols

# zdanie = input("Podaj zdanie: \n")
# print (zdanie[1:4])  

#-------------------------------------------------------------
# Zadanie 6
## Jaki będzie wynik programu:
## name = ‘Michał’
## i = 2
## print(name[i])
## ?

# name = "Michał"
# i = 2
# print(name[i])

#-------------------------------------------------------------
# Zadanie 7
## Napisz program, który wypisuje wszystkie liczby od 5 do 10.

# for i in range (5, 11):
#     print (i)

#-------------------------------------------------------------
# Zadanie 8
## Napisz program, który na ekran wypisuje 5 razy napis Hello.

# word = "Hello"
# for i in range(5):
#     print (word)
# print("---------------")
# for i in range(1,6):
#     print (word)

#-------------------------------------------------------------
# Zadanie 9
## Napisz program, który wypisuje liczby od 5 do 50, które są nieparzyste.
# for i in range ( 5 , 51 ):
#     if i% 2 == 1 :
#         print (i,end=",")
# print ( '\nSposób 2:' )
# for i in range (5, 51, 2):
#     print (i,end=",")

#-------------------------------------------------------------
# Zadanie 10
## Napisz program, który wypisuje liczby od 50 do 10 (w tej kolejności).

# for i in range (50, 9, -1):
#     print (i)

#-------------------------------------------------------------
# Zadanie 11
# Napisz program, który wypisuje wszystkie liczby od 5 do 15.

# for i in range (5, 16):
#     print (i)


#-------------------------------------------------------------
# Zadanie 12
# Napisz program drukujący na ekranie 25 gwiazdek:
# *******************

# for i in range (25):
#     print ("*", end="")
    
#-------------------------------------------------------------
# Zadanie 13
## Napisz prostą grę - zadaniem użytkownika będzie odgadnięcie liczby, którą
## zainicjujemy w programie (przykładowa liczba 600). W przypadku, gdy liczba
## będzie za duża lub za mała, użytkownik otrzyma odpowiednią podpowiedź.
## Gramy tak długo dopóki użytkownik zgadnie liczbę.

# liczba = int(600)
# odp = int(input("Podaj liczbę: \n"))
# while (odp != liczba):
#     if odp>liczba:
#         odp = int(input("Liczba jest za duża. Zgaduj dalej \n")) # tu muszą być zgodne typy - int
#     else:
#         odp = int(input("Liczba jest za mała. Zgaduj dalej \n")) # tu muszą być zgodne typy - int
# print("Twoja liczba to: ",liczba,". Gratulacje!!!")

#------- inna wwersja-------------
# import random as r 
# number = int(input('Podaj liczbę\n'))
# secret_number = r.randrange(1,10)
# while number!=secret_number:
#     if number>secret_number:
#         number = int(input('Liczba za duza\n'))
#     else:
#         number = int(input('Liczba za mala\n'))
# print('Gratulacje podales poprawna liczbe')


#-------------------------------------------------------------
# Zadanie 14
## Napisz program, który losuje 6 liczb z Dużego Lotka.
# import random as r
# ile_los = int(input("Podaj ilość losowań: \n"))
# for i in range(ile_los):
#     #sposób 1
   
#     # for i in range(6):
#     #     print (r.randrange(1,50), end=" ")
#     # print ("\n")
    
#     # #sposób 2
   
#     # for i in range(6):
#     #     print ((r).randrange(50), end=" ")
#     # print ("\n")
    
#     # #sposób 3
   
#     for i in range(6):
#         print(r.randint(1,49), end=" ")
#     print ("\n")
#     print (40*"*")
# print (40*"=")


#-------------------------------------------------------------
# Zadanie 15
## Napisz program, który prosi o podanie poprawnego hasła( hasło to Polska), tak
## długo jak użytkownik nie odgadnie hasła wyświetlany jest komunikat podaj
## poprawne hasło.

# wyraz = input("Podaj hasło: \n")
# while (wyraz != "POLSKA"):
#      wyraz = input("Błędne hasło, podaj je jeszcze raz! \n")
# print("Hasło jest prawidłowe. Witaj!!!!")   

#-------------------------------------------------------------
# Zadanie 16
# Napisz program, który odczytuje n i sumuje liczby od 1 do n. 

# liczba = int(input("Podaj liczbe: "))
# suma =0
# for i in range(1,liczba+1):  #trzeba dodać 1 bo przedział jest otwarty
#     #print ("przed:",suma)
#     suma += i
#     #print ("po:",suma)
# print (suma)


#-------------------------------------------------------------
# Zadanie 17
## Korzystając z gotowego kodu:
## import turtle
## win = turtle.Screen()
## square = turtle.Turtle()
## win.mainloop()
## Oraz dokumentacji:
## https://docs.python.org/2/library/turtle.html#turtle.forward
## Gdzie square.forward(100) rysuje 100 pikseli prosto,
## a square.left(50), zmienia położenie o 50 stopni.
## Narysuj kwadrat przy użyciu pętli for.

# import turtle
# win = turtle.Screen() # pojawia sie okno
# square = turtle.Turtle() # będziemy mieli zmienną na ktorej mozemy rysowac 

# for i in range(4):  #moze byc in range(1,5)
#     square.hideturtle() 
#     square.forward(100)
#     square.left(90)
   

# win.mainloop()

#-------------------------------------------------------------
# Zadanie 18
## Napisz program, który wypisuje co drugą literę imienia.

# name = input("Podaj imię: ")
# # # for i in range(1,(len(imie)),2):
# # #     print(imie[i], end=" ")

# for i,value in enumerate (name):
#     if i % 2 == 1 :
#         print (value)

#-------------------------------------------------------------
# Zadanie 19
## Napisz program, który odczytuje liczbę i sprawdza czy liczba jest pierwsza czy
## złożona.

# import math as m
# liczba = int(input("Podaj liczbe: "))
# pierwiastek = round(m.sqrt(liczba),2)
# if (liczba == 1):
#     print("1 nie jest liczbą pierwszą")
# elif (liczba <= 3):
#     print("To jest liczba pierwsza")
# else:
#     print("Pierwiastek kwadratowy z liczby:",liczba,", wynosi:",pierwiastek)
#     for i in range(2,int(pierwiastek)+1):
#         if (liczba%i == 0):
#             pierwsza = False
#             break
#         else:
#             pierwsza = True            
#     if pierwsza == True:
#             print("To jest liczba pierwsza")    
#     else:
#             print("To jest liczba złożona")

# #****** inny sposób ***************
# n = int ( input ( 'Podaj liczbę \n' ))
# is_prime = True
# for i in range ( 2 ,n- 1 ):
#     if n%i== 0 :
#      is_prime = False
# if is_prime:
#     print ( 'Pierwsza' )
# else :
#     print ( 'Złozona' )
# #-------------------------------------------------------------
# Zadanie 20
## Napisz program, który odczytuje wyraz i wypisuje go w odwrotnej kolejności przy
## pomocy pętli for.

# wyraz = input("Podaj wyraz: \n")

# dlWyrazu = int((len(wyraz)))

# print(dlWyrazu)

# for i in range(dlWyrazu-1,-1,-1):  #od długości wyrazu do -1 znaku ->żeby odczytać zerowy element, zeby objąć pierwszą literę i krok w dół o -1
#     print(wyraz[i],end="")          # bo liczymy od zera, np Marcin ma 6 znaków ale pozycje sa od 0 do 5

#-------------------------------------------------------------
# Zadanie 21
## Odczytaj wyraz i wypisz wszystkie cyfry występujące w wyrazie.

# wyraz = input("Podaj wyraz: \n")

# for letter in wyraz:
#     if letter.isdigit():
#         print (letter,end=",")

#-------------------------------------------------------------
# Zadanie 22
## Napisz program, który oblicza największy wspólny dzielnik dwóch liczb.
# print("Wyznaczanie Największego Wspólnego Dzielnika dwóch liczb \n ")
# LiczbaA = int ( input ("Podaj liczbe A \n "))
# LiczbaB = int ( input ("Podaj liczbe B \n "))
# #------- Sposób 1
# while LiczbaA!=LiczbaB:
#     if LiczbaA>LiczbaB:
#         LiczbaA = LiczbaA-LiczbaB
#     else :
#         LiczbaB = LiczbaB-LiczbaA
# print ("NWD sposobem 1: ",LiczbaA)

# #------- Sposób 1
# while LiczbaA!=LiczbaB:
#     if LiczbaA>LiczbaB:
#         reszta = LiczbaA % LiczbaB
#         LiczbaA = LiczbaB
#         LiczbaB = reszta
#     else :
#         reszta = LiczbaB % LiczbaA
#         LiczbaB = LiczbaA
#         LiczbaA = reszta
# print ("NWD sposobem 2: ",LiczbaA)



#-------------------------------------------------------------
# Zadanie 23
## Napisz program który wygeneruje za pomocą print (wielkość wieżyczki podaje
## użytkownik)
## a )wieżyczkę
## *
## **
## ***
## ****
## b) choinkę
##    *
##   ***
##  *****
## *******

# # Wieża
# n = int ( input ("Podaj ilośc pięter wierzy: "))
# print ( 'Wieza' )
# for i in range ( 1 ,n+ 1 ):
#     print (i* '*' )

# # Choinka
# n = int ( input ( 'Podaj n \n ' ))
# print ( 'Choinka' )
# spaces = n- 1
# for i in range ( 1 ,n+ 1 ):
#     s = spaces* ' '
#     st = '*' *( 2 *i- 1 )
#     print (s+st)
#     spaces-= 1

# wysChoinka = int(input("Podaj wysokość choinki: "))
# print("Choinka")
# pietro = 1
# wolne = int(wysChoinka-pietro)
# for i in range(1,wysChoinka+1):
#     if (pietro == 1):
#         pietro = 1
#     else:
#         pietro += 1
#     print(wolne*"-"+(pietro)*"*"+wolne*"-")
#     #print("PIetro",pietro)
#     pietro += i
#     #print("Wolne",wolne)
#     wolne -= i 
    


#-------------------------------------------------------------
# Zadanie 24
## Napisz program, który odczytuje liczbę n i na ekran wypisuje n!.

# n = int ( input ("Podaj liczbę n: " ))
# silnia = 1
# for i in range (1 ,n+1):
#     silnia *=i
# print("Silnia = ",silnia)

#-------------------------------------------------------------
# Zadanie 25
## Napisz program, który sprawdza czy wyraz jest palindromem przy
## użyciu pętli while.


# word = input ( 'Podaj slowo \n' )
# is_palindrom = True                 #zmienna pomocnicza przyjmuje wartość TRUE
# left = 0                            #ustalamy początkową wartość zmiennej left na 0, aby móc odczytac pierwszą(zerową) literę ciągu
# right = len (word)- 1               #zmienna right przyjmuje wartość odpowiadającą numerowi ostatniej litery ciagu (-1, bo liczymy od zera)
# print(word[left],"- z lewej")
# print(word[right],"- z prawej")
# while left!=right:                  # do chwili gdy pierwsza i ostatnia ( a następnie kolejne druga i przedostatnia itd.) litera ciągu sa takie same wykonuj pętle while, zakończ gdy będą różne 
#     if word[left]!=word[right]:     # sprawdź czy pierwsza i ostatnia litera (i odpowiednio kolejne) są różne
#         is_palindrom = False        # jeżeli tak, to przypiz zmiennej is_palindrom wartość False
#         break                       # i zakończ pętlę
#     left+= 1                        # zmień wartość zmiennej left o 1 - aby sprawdzic następną literę ciągu(od lewej)
#     right-= 1                       # zmień wartość zmiennej right o -1 (w dół) - aby sprawdzic następną literę ciągu(od prawej) i porównać je w pętli while i w ifie
#     print(word[left],"- z lewej")
#     print(word[right],"- z prawej")

# print (is_palindrom)                # wyświetl wartość zmiennej is_palindrom na ekranie w zaleznosci jaka otrzymala ona wartoś


## ----- bez pętli ------
# wyraz = input("Podaj wyraz: \n")
# # print (wyraz[::-1])
# wyrazOdwr = wyraz[::-1]
# print("Wyraz odwrócony:",wyrazOdwr)
# if wyraz == wyrazOdwr:
#     print("TAK - wyraz jest palindromem")
# else:
#     print("NIE - wyraz nie jest palindromem")


#-------------------------------------------------------------
# Zadanie 26  - SPRWDZIĆ!!!!!
# Napisz program, który odczytuje liczbę n i na ekran wypisuje n-ty
# wyraz ciągu Fibonacciego:


# n = int ( input ( 'Podaj liczbę n' ))
# a = 1 # first
# b = 1 # second
# for i in range ( 3 ,n+ 1 ):
#     c = b
#     b = a+b
#     a = c
# print (b)

# zakres = int(input("Podaj zakres ciągu Fibonacciego: "))
# pierwsza = 1
# druga = 1
# for i in range (1,zakres+1):
#     pom = pierwsza + druga
#     kolejna = druga + pom
# print(kolejna)
