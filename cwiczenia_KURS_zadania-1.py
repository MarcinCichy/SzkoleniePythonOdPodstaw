#-------------------------------------------------------------
# Zadanie 1
## Kostka do gry.
## Napisz program, który losuje liczbę, która może pojawić się na kostce do gry,
## czyli liczbę od 1 do 6.

# import random as r
# print(r.randrange(1,7))

#-------------------------------------------------------------
# Zadanie 2
## Odczytaj wyraz i na ekranie wypisz Hello Nazwa Wyrazu (odzielone spacją).

# wyraz = input("Podaj wyraz: \n")
# print ("Hello", wyraz )

#-------------------------------------------------------------
# # Zadanie 3
## Ania chce urządzić przyjęcie urodzinowe. Chce podzielić cukierki równo dla
## gości, a dla siebie zostawić resztę. Powiedz Justynie ile zostanie dla niej
## cukierków.
## Przykład:
## Podaj liczbę gości:
## 10
## Podaj liczbę cukierków.
#3 32
## Dla Justyny zostaną 2 cukierki.

# ile_gosci=int(input("Podaj liczbe gosci: \n"))
# ile_cukierkow=int(input("Podaj liczbe cukierkow: \n"))

# reszta = ile_cukierkow%ile_gosci
# print("Justyna dostanie", reszta, "cukierków")

#-------------------------------------------------------------
# Zadanie 4
## Wydrukuj za pomocą print 20 gwiazdek w jednej lini.
## ********************

# print ("*"*20)

#-------------------------------------------------------------
# Zadanie 5
## Odczytaj liczbę i pokaż na ekran liczbę cyfr danej liczby.
## Przykład:
## Podaj liczbę
## 200
## Liczba ma 3 cyfry.

# liczba = str(input("Podaj liczbę: \n"))
# print(liczba ,"ma", len(liczba), "znakow")

#-------------------------------------------------------------
# Zadanie 6
## Odczytaj liczbę i wypisz na ekran 10*liczba. Uwzględnij niepoprawne dane.
## Przykład dla danych
## 20
## Wynik:
## 200
## Dla danych
## Aaa
## Wynik:
## To nie jest poprawna liczba

# try:
#     liczba = input("Podaj liczbe: \n")
#     print (int(liczba)*10)
# except:
#     print("To nie jest poprawna liczba")

#-------------------------------------------------------------
# Zadanie 6 - inna wersja

# try:
#     liczba = int(input("Podaj liczbe: \n"))
#     print (liczba*10)
# except:
#     print("To nie jest poprawna liczba")

#-------------------------------------------------------------
# Zadanie 7
## Odczytaj wyraz i wypisz pierwszą literę wyrazu.

# wyraz = input("Podaj wyraz: \n")
# print('Pierwsza litera to:',wyraz[0])

#-------------------------------------------------------------
# Zadanie 8
## Odczytaj liczbę i sprawdź czy liczba jest parzysta, czy nieparzysta.

# liczba = int(input("Podaj liczbę: \n"))
# if liczba%2 == 0:
#     print ("Liczba jest parzysta")
# else:
#     print ("Liczba jest nieparzysta")

#-------------------------------------------------------------
# Zadanie 9
## Odczytaj wiek danej osoby i sprawdź czy osoba jest nastolatkiem.
## Zakładamy, że osoba jest nastolatkiem jeśli ma od 13 do 17 lat.

# wiek = int(input("Podaj swój wiek: \n"))

# if (wiek >= 13) and (wiek <= 17):
#     print ("Jestes nastolatkiem")
# elif (wiek < 13):
#     print ("Jesteś małolatem")
# else:
#     print("Staruszek z ciebie ")

##************* inna wersja **********
# try:
#     age = int(input('Podaj wiek'))
#     message = 'jesteś nastolatkiem'
#     if age>13 and age<18:
#      print(message)
#     else:
#      print('Nie',message)
# except:
#     print('Niepoprawne dane')

#-------------------------------------------------------------
# Zadanie 10
## Odczytaj liczbę i sprawdź czy dana liczba jest podzielna przez 8.

# liczba = int(input("Podaj liczbę: \n"))
# if liczba%8 == 0:
#     print ("Liczba jest podzielna przez 8")
# else:
#     print ("Liczba nie jest podzielna przez 8")

# -------------------------------------------------------------
# Zadanie 11
## Napisz program, który odczytuje wyraz i sprawdza czy pierwsza litera to M.

# wyraz = input("Podaj wyraz: \n")
# if (wyraz[0]=='M') or (wyraz[0]=='m'):
#     print("Pierwsza litera to M")
# else:
#     print("Pierwsza litera to nie jest M")

# -------------------------------------------------------------
# Zadanie 12
## Odczytaj wyraz i wypisz na ekran wartość True lub False w zależności od tego
## czy wyraz zawiera w sobie napis kot

# wyraz = input("Podaj wyraz: \n") 
# if ('kot' in wyraz):
#     print('TRUE') 
# else:
#     print('FALSE')

#-------------------------------------------------------------
# Zadanie 13
## Napisz program, który odczytuje wyraz i zamienia go na małe litery:
## Dane:
## AKADEMIA
## Wynik:
## akademia

# wyraz = input("Podaj wyraz: \n") 
# print ("Wyraz pisany dużymi literami:", wyraz.upper())
# print ("Wyraz pisany małymi literami:", wyraz.lower())

#-------------------------------------------------------------
# Zadanie 14
## Napisz program, który odczytuje wyraz i sprawdza czy wprowadzony wyraz
## to Akademia.

# wyraz = input("Podaj wyraz: \n")
# if (wyraz == 'AKADEMIA') or (wyraz == 'akademia'):
#      print("Podany wyraz to",wyraz)

# ------ inna wersja ---------

# wyraz = input("Podaj wyraz: \n")
# while (wyraz.lower() != "akademia"):
#      wyraz = input("Podaj wyraz jeszcze raz! \n")
# print("Podany wyraz to",wyraz)   

#-------------------------------------------------------------
# Zadanie 15
## Odczytaj wyraz i sprawdź czy ostatnia litera to M bądź m.

# wyraz = input("Podaj wyraz: \n")
# if (wyraz[-1]=='M') or (wyraz[-1]=='m'):
#     print("Ostatnia litera to M")
# else:
#     print("Ostatnia litera to nie jest M")

#-------------------------------------------------------------
# Zadanie 16
## Odczytaj 2 liczby i wypisz na ekran największą z liczb.


# liczba1 = int(input("Podaj liczbe A: \n"))
# liczba2 = int(input("Podaj liczbe B: \n"))
# if liczba1 > liczba2:
#     print ("Wiekszą jest liczba A=",liczba1)
# elif liczba1<liczba2:
#     print ("Wiekszą jest liczba B=",liczba2)

#-------------------------------------------------------------
# Zadanie 17  !!!!! sprawdzic
## Odczytaj 3 liczby i wypisz na ekran największą z liczb.

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
# Zadanie 18
## Odczytaj 2 liczby i wypisz na ekran średnią z liczb.

# liczba1 = float(input("Podaj liczbe A: \n"))
# liczba2 = float(input("Podaj liczbe B: \n"))
# print ('Średnia z liczby A i B, to: ',0.5*(liczba1+liczba2))

#-------------------------------------------------------------
#  Zadanie 19
## Odczytaj imię i sprawdź czy imię jest męskie czy żeńskie.
## Uwzględnij wyjątek Barnaba.

# name = input("Podaj imię: \n")
# if (name == 'Barnaba') or (name == 'Kuba') or (name == 'Bonaventura'):
#     print (name, "to wyjątkowe imię męskie kończące sie na literę a")
# elif  (name[-1] == 'a'):
#     print("Podane imię jest żeńskie")
# else:
#     print("Podane imię jest męskie")

#-------------------------------------------------------------
# Zadanie 20
## Odczytaj 2 liczby, gdzie podane są przyprostokątne trójkąta, na ekran wypisz
## przeciwprostokątną.

# import math as m
# przyprostokatna1 = int(input("Podaj pierwszą przyprostokątną trójkąta: \n"))
# przyprostokatna2 = int(input("Podaj drugą przyprostokątną trójkąta: \n"))
# print('Przeciwprostokątna wynosi:', round(m.sqrt(pow(przyprostokatna1,2)+pow(przyprostokatna2,2)),2))


#-------------------------------------------------------------
# Zadanie 21
## Odczytaj liczbę i wypisz odwrotność danej liczby.

# liczba = int(input("Podaj liczbe : \n"))
# print(1/liczba)

#-------------------------------------------------------------
# Zadanie 22
## Napisz program, który losuje liczbę losową z przedziału 1..100.

# import random as r
# print (r.randrange(1,101))    #pierwszy sposób oznaczenia przedziału
# print("\n")
# print (r.randrange(100)+1)    #drugi sposób oznaczenia przedziału
# print("\n")
# print(r.randint(1,100))       #trzeci sposób oznaczenia przedziału

#-------------------------------------------------------------
# Zadanie 23
## Napisz program, który oblicza pole koła.

# import math as m
# r = float(input("Podaj promień koła :\n"))
# print ("Pole koła wynosi:",round((m.pi*r**2),2))

#-------------------------------------------------------------
# Zadanie 24
## Napisz program, który odczytuje wyraz i sprawdza czy pierwsza litera to A
## Dane:
## Adam
## Wynik:
## True
## Dane2:
## Piotr
## Wynik:
## False

# wyraz = input("Podaj wyraz: \n")
# if (wyraz[0]=='A') or (wyraz[0]=='a'):
#     print(True)
# else:
#     print(False)

##*************** inna wersja ********
# word = input('Podaj wyraz\n')
# print(word[1]=='A')

#-------------------------------------------------------------
# Zadanie 25
## Odczytaj 2 wyrazy i sprawdź czy wprowadzone wyrazy są równe.
## Dla wywołania:
## Ala Ala
## Wynikiem powinno być tak.
## Dla wywołania:
## Ala Sak
## Wynikiem powinno być nie.

# wyraz1 = input("Podaj pierwszy wyraz \n")
# wyraz2 = input("Podaj drugi wyraz \n")

# if wyraz1 == wyraz2:
#     print("tak")
# else:
#     print("nie")

#-------------------------------------------------------------
#  Zadanie 26
## Odczytaj wyraz i sprawdź czy wyraz jest palindromem.
## Dane:
## kok
## Wynik:
## Tak
## Dane:
## Mama:
## Wynik:
## Nie.

# wyraz = input("Podaj wyraz: \n")
# # print (wyraz[::-1])
# wyrazOdwr = wyraz[::-1]
# print("Wyraz odwrócony:",wyrazOdwr)
# if wyraz == wyrazOdwr:
#     print("TAK - wyraz jest palindromem")
# else:
#     print("NIE - wyraz nie jest palindromem")

#-------------------------------------------------------------
# Zadanie 27
## Odczytaj 2 liczby, jako wynik wypisz potęgę.
## Przykładowo dla danych:
## 2
## 10
## Wynikiem powinno być:
## 1024

# liczbaA = int(input("Podaj liczbe A: \n"))
# liczbaB = int(input("Podaj liczbe B: \n"))
# print("LIczba",liczbaA,"podniesiona do potęgi",liczbaB,"wynosi:",liczbaA**liczbaB)

#-------------------------------------------------------------
# Zadanie 28
## Odczytaj wyraz i wypisz drugą literę wyrazu.

# wyraz = input("Podaj wyraz: \n")
# print("Druga litera wyrazu",wyraz,"to:",wyraz[1])

#-------------------------------------------------------------
# Zadanie 29
## Odczytaj wyraz i zamień * pustym ciągiem.
## Przykładowo dla ciągu znaków a*bcd ma być wypisany wyraz abcd.

# wyraz = input("Podaj wyraz: \n") 
# nowyWyraz = ""
# ASTERIX = "*"                    # utworzenie stałej - dlatego jeje nazwa jest zapisana dużymi literami

# for letter in wyraz:            # iteracja po ciągu wg. zmiennej 'letter' wskazującej na kolejny znak w ciagu 'wyraz'
#     if letter not in ASTERIX:   # jeżeli wartość zmiennej 'letter' nie jest równa stałej ASTERIX 
#         nowyWyraz += letter     # to tworzony jest nowy ciąg poprzez konkatenację kolejnych liter z ciągu, ale bez '*'
# print(nowyWyraz)                # wyswietla ostateczny wynik kokatenacji (po przejściu całej pętli - tyle razy ile jest liter w wyrazie)


##********* inna wersja **********
# word = input('Podaj wyraz\n')
# print(word.replace('*',''))

#-------------------------------------------------------------
# Zadanie 30
## Wypisz True jeśli wyraz kończy się wyrazem “tka” bądź False jeśli wyraz nie
## kończy się na wyrazie “tka”.

# wyraz = input("Podaj wyraz: \n")
# dlWyrazu = int((len(wyraz)))                  # oblicza dłogość ciągu 'wyraz'
# print(dlWyrazu)                             # tylko sprawdzenie - dla mnie - wypisuje z ilu liter składa się ciąg 'wyraz'
# # print (wyraz[dlWyrazu-3:dlWyrazu])          # tylko sprawdzenie - dla mnie - wypisuje trzy ostatnie litery ciągu 'wyraz'
# trzyOstatnie = wyraz[dlWyrazu-3:dlWyrazu]     # przypisanie do zmiennej 'trzyOstatnie' ostatnich 3 liter z ciągu 'wyraz'
# # print (trzyOstatnie)                        # tylko sprawdzenie - dla mnie - wypisuje wartośc zmiennej 'trzyOstatnie' - wiem wtedy czy dobrze to zrobiłem
# if trzyOstatnie == "tka":                     # jeżeli zmienna 'trzyOstatnie' równa jest wartości 'tka'
#     print(True)                               # to wypisz 'True'
# else:                                         # w przeciwnym wypadku
#     print(False)                              # wypisz 'False'


##****** inna wersja **********

# word = input('Podaj wyraz\n')
# print(word.endswith('tka'))