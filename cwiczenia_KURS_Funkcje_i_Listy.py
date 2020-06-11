#-------------------------------------------------------------
# MOJEZAD

# lista=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24],[25,26,27,28]]
# for i in range(0,7):   #
#         print("Lista nr:",i)
#         print(lista[i])
#         print("Elementy listy",i,":",end=" ")
#         for j in range(0,4):
#             print(lista[i][j],end=" ")
#         print("\n-------------------")


# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()

#-------------------------------------------------------------
# Zadanie 1
#-----------
## Napisz metodę add wyznaczającą sumę dwóch zadanych liczb całkowitych. Napisz
## program wykorzystujący funkcję add.


# def add(A,B):
#     C=None
    
#     C=A+B
#     print(C)
#     return
    
# A = int(input("Podaj pierwszą liczbę: "))
# B = int(input("Podaj drugą liczbę :"))

# add(A,B)


#-------------------------------------------------------------
# Zadanie 2
#-----------
## Napisz funkcję subtraction wyznaczającą różnicę dwóch zadanych liczb
## całkowitych. Działanie funkcji sprawdź pisząc odpowiedni program.

# def substraction(A,B):
#     C=None
    
#     C=A-B
#     print(C)
#     return
    
# A = int(input("Podaj pierwszą liczbę: "))
# B = int(input("Podaj drugą liczbę :"))

# substraction(A,B)

#-------------------------------------------------------------
# Zadanie 3
#-----------
## Napisz funkcję multiply wyznaczającą iloczyn dwóch zadanych liczb całkowitych.
## Działanie funkcji sprawdź pisząc odpowiedni program.

# def multiply(A,B):
#     C=None
    
#     C=A*B
#     print(C)
#     return
    
# A = int(input("Podaj pierwszą liczbę: "))
# B = int(input("Podaj drugą liczbę :"))

# multiply(A,B)

#-------------------------------------------------------------
# Zadanie 4
## Napisz funkcję divide wyznaczającą iloraz dwóch zadanych liczb całkowitych.
## Działanie funkcji sprawdź pisząc odpowiedni program. Dla chętnych *- Napisz
## funkcję z obsługą błędów.

# def divide(A,B):
   
#     if B != 0:
#         C=A/B
#         print(round((C),2))
#     else:
#          print("Pamietaj cholero. Nie dziel przez zero!!")
        
#     return
    
# A = float(input("Podaj pierwszą liczbę: "))
# B = float(input("Podaj drugą liczbę :"))

# divide(A,B)

#-------------------------------------------------------------
# Zadanie 5
#-----------
# Napisz funkcję,, która ma trzy parametry formalne a, b, c będące liczbami
# całkowitymi. Funkcja zwraca prawdę, jeśli zadane liczby są liczbami pitagorejskimi
# oraz fałsz w przeciwnym wypadku. Liczby pitagorejskie spełniają warunek:
# a*a+b*b=c*c.

# # ------- SOSÓB 1 -------------------
# def pitagorejskie(a,b,c):
#     if (a*a+b*b) == c*c:
#         pitagorejskie = True
#     else:
#         pitagorejskie = False

#     return pitagorejskie

# wynik = pitagorejskie(5,4,3)
# print("Sposób 1:",wynik)


# ## ------- SOSÓB 2 -------------------

# def pitagorejskie2(d,e,f):
#     if (d*d+e*e) == f*f:
#         pitagorejskie2 = True
#     else:
#         pitagorejskie2 = False
#     print("Sposób 2:",end=" ")
#     if pitagorejskie2:
#         print("Prawda")
#     else:
#         print("Fałsz")

# pitagorejskie2(2,3,4)



# ## ------- SOSÓB 3  właściwy - kontrola błędów -------------------
# def is_pythagorean(a,b,c):
#     if a<0 or b<0 or c<0:
#         return False
#     array = [a,b,c]
#     array.sort()
#     if array[0]*array[0]+array[1]*array[1]==array[2]*array[2]:
#         return True
#     else:
#         return False

# a = int(input('Podaj liczbe 1\n'))
# b = int(input('Podaj liczbe 2\n'))
# c = int(input('Podaj liczbe 3\n'))
# ## if is_pythagorean(a,b,c) ==True tak samo
# if is_pythagorean(a,b,c):
#     print('TAK')
# else:
#     print('NIE')
## is_pythagorean(5,4,3)
## is_pythagorean(3,4,5)
#-------------------------------------------------------------
# Zadanie 6
#-----------
## Napisz funkcję sprawdzającą czy liczba jest parzysta.


# def even(number):
#     #return number%2==0  #-> może być krócej
#     if number % 2 == 0:
#         return even
    


# number = int(input("Podaj liczbę: "))

# check = even(number)
# print(check)
# if check:
#     print("Liczba jest parzysta")
# else:
#     print("Liczba jest nieparzysta")

# if even(number):            # -> if even(number) == True:
#     print("Parzysta")
# else:
#     print("Nieparzysta")


#-------------------------------------------------------------
# Zadanie 7
#-----------
## Napisz funkcję, która wyznacza sumę cyfr liczby całkowitej.

# def suma_cyfr(number):
#     size = len(number)
#     lista = []
#     suma = 0
#     for i in range(size):
#         lista.append(number[i])
#         suma += int(lista[i])
#     return suma

# number = input("Podal liczbę całkowitą: ")
# suma_koncowa = suma_cyfr(number)
# print(suma_koncowa)

#liczba%10 -> ostatnia cyfra

#-------------------------------------------------------------
# Zadanie 8
## Napisz funkcję, która stwierdza, czy zadana jako parametr liczba całkowita jest
## kwadratem pewnej liczby całkowitej. Liczby będące kwadratami liczb całkowitych
## to 1, 4, 9, 16 itd. Wartością funkcji ma być prawda, jeśli liczba spełnia warunek oraz
## fałsz w przeciwnym wypadku.

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



## wersja mm
# import math
# # math.isqrt(5))
# # 16 4 - 4 = 0
# # 17 4.5 -4 !=0
# # dla osób w wersji 3.82
# # def is_square(n):
# #     return n == math.isqrt(n)*math.isqrt(n)
# def is_square(n):
#     sqrt = math.sqrt(n)
#     return (sqrt - int(sqrt) ==0)
# print(is_square(16))
# print(is_square(17))
#-------------------------------------------------------------
# Zadanie 9
## Napisz funkcję, która zwraca sumę dwóch stringów.
## sum(“aaa”,”bb”) powinno zwrócić “aaabb”

# def funkcja(string1,strin2):
#     sum_string = string1+string2
#     return sum_string

# string1 = input("Podaj pierwszy ciąg: ")
# string2 = input("POdaj drugi ciąg: ")
# suma_ciagow = funkcja(string1,string2)
# print(suma_ciagow)


#-------------------------------------------------------------
# Zadanie 10
## Napisz funkcję, która zwraca maksymalną długość 2 stringów.
## maxStringLength(“aaaa”,”sad”) zwróci 4.
## maxStringLength(“aaksadui”,”aaa”) zwróci 8.


# def max_lenght(string1,string2):
#     lista=[]                      # tworzę pustą listę, do której będe dodawał wyniki z wyznaczania długości poszczególnych stringów
#     lenght1 = len(string1)        # obliczam długość pierwszego stringu
#     lista.append(lenght1)         # dodaje wynik obliczania do listy
#     lenght2 = len(string2)        # obliczam długość drugiego stringu
#     lista.append(lenght2)         # dodaje wynik drugich obliczeń do listy
#     maximum = max(lista)          # wyznaczam maksymalna wartość z dwóch wartości(wyznaczone długości stringów)
#     return maximum                # zwracam wynik max


# string1 = input("Podaj pierwszy ciąg: ")
# string2 = input("POdaj drugi ciąg: ")

# wynik = max_lenght(string1,string2)
# print("Maksymalna długość dwóch podanych ciągów,to:",wynik)


#-------------------------------------------------------------
# Zadanie 11
## Napisz funkcję, która odczytuje jako argument liczbę i wypisuje liczbę dzielników.


# def numbers_of_dividers(number):
#     score = 0                             # tworze zmienną pomocnicz a i przyppisuje jej wartośc 0
#     for i in range(1,number+1):           # petla sprawdza wszystkie dzielniki od 1 do wartości zadanej liczby
#         if number%i == 0:                 # sprawdzam warunek, czy modulo zadanej liczby przez kolejny dzielnik jest równe 0
#             score += 1                    # jeżeli tak, to zwiększam wartośc pomocniczej zmiennej o 1, bo znaleziony został dzielmnik 
#     return score                          # zwracam wartośc zmiennej pomocniczej, jako ilość znalezionych dielników

# number = int(input("Podaj liczbę: "))
# result = numbers_of_dividers(number)
# print("Ilość dzielników liczby ",number,", wynosi:",result)


#-------------------------------------------------------------
# Zadanie 12
## Napisz funkcję, która stwierdza, czy zadana jako parametr liczba całkowita jest
## sześcianem pewnej liczby naturalnej.


# import math
# def szescian(liczba):
#     pierw_trz_st = round(pow(liczba,0.3333),2)          #pierwiastek to liczba podniesiona do potęgi, będącą odwrotnością stopnia pierwiastka
#     print("Pierwiastek sześcienny z podanej liczby",liczba,"wynosi: ",pierw_trz_st)
#     is_pierwiastek = True             #zakładam, że piwiatek jest prawdziwy
#     if pierw_trz_st%1 != 0:                      # jeżeli modulo z dzielenia przez 1 jest różne od zera, to nie jest to liczba całkowita
#            is_pierwiastek = False                 # i pierwiastek jest fałszywy
#     return is_pierwiastek                         # zwraca wartosc pierwiastka
  
# try:
#     liczba = int(input("Podaj liczbę do spawdzenia: "))
#     wynik = szescian(liczba)
#     print ("Czy podana liczba: ",liczba,", jest sześcianem liczby całkowitej? ->",wynik)
# except:
#     print("To nie jest liczba naturalna")



# import math
# def szescian(liczba): 
#     while not liczba.numeric():           #liczba.numeric() - czy liczba jest naturalna
#         liczba = input("To nie jest liczba naturalna. \nPodaj jeszcze raz: ")
#     else:
#         pierw_trz_st = round(pow(int(liczba),0.3333),2)
#         print("Pierwiastek szescienny z podanej liczby",liczba,"wynosi: ",pierw_trz_st)
#         is_pierwiastek = True
#         if pierw_trz_st%1 != 0:                      # jeżeli modulo z dzielenia przez 1 jest różne od zera, to nie jest to liczba całkowita
#             is_pierwiastek = False
#         return is_pierwiastek
          
        
  
# liczba = input("Podaj liczbę do sprawdzenia: ")
# print ("Czy podana liczba, jest sześcianem liczby całkowitej? ->",szescian(liczba))




# def is_it_quibc(arg_1):
#     return(round(pow(arg_1,1/3),6) % 1 == 0)  # zwróć wartość zmiennej arg_1 podniesionej do odwrotnosci stopnia pierwiastka i zaokraglonej do 6 m po przecinku
                                                # jezeli modulo tego pierwiastka przez 1 jest rowne 0
# try:
#     number_1 = int(input('Provide number : '))
#     print('Is it quibic :', is_it_quibc(number_1))
# except:
#     print('Incorrect value!')

#-------------------------------------------------------------
# Zadanie 13
## Napisz funkcję, która stwierdza, czy zadana jako parametr liczba całkowita jest
## liczbą pierwszą.
## ******************* 
# jest podzielone na dwa pliki i zastosowany jest tu import


#nowe
# sposób 1 -> importujemy jedną funkcję z innego pliku
# from zad11 import numbers_of_dividers     #import tylko jednej funkcji do spradzenia liczby dzielników zpliku zad11

# print(numbers_of_dividers(5))

# # sposób 2 -> 
# import zad11 as s   # tu importujemy cały plik zad11
# print(s.numbers_of_dividers(5)) #jako metoda numbers_of_dividers pochodząca z s(zad11)


# # tu rozwiązanie zadania

# import zad11 as s 
# def is_prime(number):                           # jeżeli liczba ma więcej niz 2 dzielniki to nie jest pierwsza
#     return s.numbers_of_dividers(number) == 2   # zwraca wrtosc zaimportowanej funkcji jezeli jej wynik jest rowny 2, czyli liczba ma tylko 2 dzielniki(wtedy jest pierwsza)
# print(is_prime(10))


#-------------------------------------------------------------
# Zadanie 13
## Napisz funkcję, która stwierdza, czy zadana jako parametr liczba całkowita jest
## liczbą pierwszą.
## ******************* 

# import math as m

# def pierwsza(liczba):
    
#     pierwiastek = round(m.sqrt(liczba),2)
#     if (liczba == 1):
#         #print("1 nie jest liczbą pierwszą")
#         pierwszaL = False
#     elif (liczba <= 3):
#         #print("To jest liczba pierwsza")
#         pierwszaL = True
#     else:
#         #print("Pierwiastek kwadratowy z liczby:",liczba,", wynosi:",pierwiastek)
#         for i in range(2,int(pierwiastek)+1):
#             if (liczba%i == 0):     #???????
#                 pierwszaL = False
#                 break
#             else:
#                 pierwszaL = True            
#     if pierwszaL == True:
#             return True   
#     else:
#             return False


# liczba = int(input("Podaj liczbe: "))
# wynik = pierwsza(liczba)
# print("Czy podana liczba,",liczba,"jest liczbą pierwszą? ->",wynik)


#-------------------------------------------------------------
# Zadanie 14  - dokończyć!!!!!
## Skorzystaj z wcześniejszej funkcji (zad.11.) do znalezienia liczby od 2 do 10000, która
## ma największą liczbę dzielników.


# def numbers_of_dividres(number):
#     score = 0
#     for i in range(1,number+1):
#         if number%i == 0:
#             score += 1
#     return score


# from zad11 import numbers_of_dividers

# dictionary ={}
# dict2 ={}
# for number in range(2,10001):
#     dictionary[number]=numbers_of_dividers(number)
#     maximum_value = max(dictionary.values()) 
# # print("Maksymakna ilość dzielników, poraz pierwszy:",maximum_value)
# for keys,values in dictionary.items():
#     if values == maximum_value:
#         dict2[keys] = values

# # print("Słownik z mak. il. dzielników:",dict2)
# # print("Maksymakna ilość dzielników:",maximum_value)
# lista_kluczy=dict2.keys()
# print("Największa liczba dzielników, to:",maximum_value,"i występuje dla liczb(y) :",lista_kluczy)



#-------------------------------------------------------------
# Zadanie 15
## Napisz funkcję, która sprawdza czy dany wyraz jako argument jest palindromem.

# def isPalindrome(word):
#     left = 0
#     right = len (word)- 1
#     is_palindrom = True
#     while left<right:
#         if word[left]!=word[right]:
#             is_palindrom = False
#             break
#         left+= 1
#         right-= 1
#     # print (is_palindrom)   
#     # if is_palindrom:
#     #     print ( 'Palindrom' )
#     # else :
#     #     print ( 'To nie jest palindrom' )
#     return is_palindrom


# word = input ( 'Podaj wyraz \n ' )
# print("Czy wraz",word,"jest palindromem? ->",isPalindrome(word))


#-------------------------------------------------------------
# Zadanie 16
## Napisz funkcję, która sprawdza czy wyraz jest peselem. Dla uproszczenia
## sprawdzamy czy każdy znak jest cyfrą i czy wyraz ma 11 znaków.
## isPesel(“87122508076”)

# def isPESEL(number):
#     if  len(number) != 11 or not number.isdigit():                    #liczba.isdigit() sprawdza czy liczba jest cyfrą
#         print("To nie jest właściwy numer PESEL. Podaj jeszcze raz")
#         PESEL = False
#     else:
#         PESEL = True
#     return PESEL

# z pętlą do upadłego proszącą o wpisanie poprawnego nr PESEL
# def isPESEL(numbPESEL):
#     PESEL = True
#     while len(numbPESEL) != 11 or not numbPESEL.isdigit():
#         numbPESEL = input("To nie jest właściwy numer PESEL. Podaj jeszcze raz: \n")
#         PESEL = False
#     return PESEL
    
# numbPESEL = input("Podaj PESEL: \n")
# if isPESEL(numbPESEL): print("To jest właściwy PESEL")


### wersja Darka
# def isPesel(x):
#     if len(x)==11 and x.isnumeric():
#         return True
#     else:
#         return Falsepesel = input('Podaj PESEL:\n')
# print(isPesel(pesel))
#-----------------
# def isPesel2(x):
#     if len(re.findall('[0-9]', pesel))==11:
#         return True
#     else:
#         return False
#-------------------------------------------------------------
# Zadanie 17
## Napisz funkcję, która dla danej tablicy liczb całkowitych zwraca pierwszy element
## tablicy.
## first([1,2,3,4]) = 1
## first(4,9,12,1]) = 4


# def first(*arg):
#     print("Pierwszym elementem tablicy jest:",arg[0])


# first(*[1,2,3,4])
# first(*[4,9,12,1]) 


# #rozwiązanie MM
# def first ( array ):
#     return array[ 0 ]

# print (first([ 1 , 2 , 3 , 4 ]))

#-------------------------------------------------------------
# Zadanie 18
## Napisz funkcję, która dla danej tablicy liczb całkowitych zwraca ostatni element listy..

# def last(*arg):
#     print("Ostatnim elementem tablicy jest:",arg[-1])


# last(*[1,2,3,9])
# last(*[4,9,12,11]) 

# #rozwiązanie MM
# def last ( array ):
#     return array[- 1 ]

# print (last([ 1 , 2 , 3 , 4 ]))

#-------------------------------------------------------------
# Zadanie 19

## Napisz funkcję, która jako argument przyjmuje zawsze listy składającą się z
## dwóch elementów liczb całkowitych. Metoda ma zwróci sumę elementów listy.
## sum([1,2]) = 3
## sum([4,8]) = 12


# def sum(*arg):
#     if len(arg) != 2:
#         print("Nieprawidłowa długosć listy")
#     else:
#         print(arg[0]+arg[1])


# sum(*[1,2])
# sum(*[4,8])



#-------------------------------------------------------------
# Zadanie 20
## Napisz funkcję, która dla danej listy zwraca sumę pierwszego i ostatniego
## elementu tablicy. sumArray([1, 2, 3]) = 1+2 = 3


# def first(*arg):
#      return arg[0]

# def last(*arg):
#     return arg[-1]

# def sum(*arg):
#     if len(arg) != 3:
#         return print("Nieprawidłowa długosć listy")
#     else:
#         return first(*arg)+last(*arg)
        


# print(sum(*[1,2,17]))

# #rozwiązanie MM

# def sumArray ( a ):
#     return a[ 0 ]+a[- 1 ]

# print (sumArray([ 1 , 2 , 3 ]))

#-------------------------------------------------------------
# Zadanie 21 

# Napisz funkcję, która zwraca element środkowy listy.
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
# def middleElement(*arg):
#     # print(sum(arg))
#     # print (len(arg))
#     # print (len(arg)//2)
#     lenght = len(arg)
#     if lenght%2 == 1:
#         return arg[lenght//2]       # jezeli reszta z dzielenia przez 2 jest 1 to jest to środek dla nieparzystej ilosci elementów
#     else:
#         return arg[lenght//2-1]     ## jezeli reszta z dzielenia przez 2 jest różna od 1 to jest to środek 
#     #return int(sum(arg)/len(arg))  ## dla parzystej ilosci elementów i zaokrąglony w dól BO MOZE BYC ŚRODEK Z LEWEJ LUB Z PRAWEJ
    
 
# print("Środkowy element listy to:",middleElement(*[1, 5, 3, 4,6])) 


#-------------------------------------------------------------
# Zadanie 22
## Zakładamy, że mamy 2 listy 2 elementowe. Nasza funkcja powinna zwrócić nową
## listę, która jest połączona z dwóch list.
## plusTwoArrays([-4, 4], [8, 2]) → [-4, 4, 8, 2]
## plusTwoArrays([9, 1], [3, 10]) → [9, 1, 3, 10]


# def  plusTwoArrays(array1,array2):
#     #sumOfArrays = array1+array2
#     return array1+array2

# print(plusTwoArrays([-4, 4], [8, 2]))
# print(plusTwoArrays([9, 1], [3, 10]))

# # #rozwiązanie MM
# def plusTwoArray ( a , b ):
#     return [a[ 0 ],a[ 1 ],b[ 0 ],b[ 1 ]]

# print (plusTwoArray([ 2 , 2 ],[ 3 , 4 ]))

#-------------------------------------------------------------
# Zadanie 23
## Napisz funkcję, która zwraca sumę elementów listy całkowitej.
## sum([1,2,3]) = 6


# def sum(arg):
#     suma=0
#    # print(len(arg))
#    # moze być for i in arg
#     for i in range(0,len(arg)):     # może być od 0 do len(arg), bo len(arg) daje wynik od 1 do n (ilość elemntów)
#         suma += arg[i] 
#         #print(suma)            # asumownie jest o 0 do n-1. NP długośc list do 7(od 1 do 7), a sumowanie jest od 0 do 6
#     return suma                     # bo nie domknięty jest górny przedział, czyli 7-1=6 (n-1)


# print(sum([1,2,3,4,5,-2,12,5]))


#-------------------------------------------------------------
# Zadanie 24
## Napisz funkcję, która zwraca największy element listy całkowitej.
## max([2,3,5,1,20,25]) = 25

# def maximum(array):
#     return max(array)


# print(maximum([2,3,5,1,20,25]))


# # #rozwiązanie MM
# def max ( a ):
#     result = a[ 0 ]
#     for i in a:
#         if i>result:
#             result = i
#     return result

# print ( max ([- 9 , 12 , 2 ]))

#-------------------------------------------------------------
# Zadanie 25
## Napisz funkcję, która odwraca daną tablicę liczb całkowitych.
## swap([1,2,3]) = [3,2,1]

# def swapx(array):
#     # print(array[::-1])
#     # odwr = array.reverse()
#     # print(odwr)
#     return array[::-1]

# #----- inny sposóbb ---------
# def swap(array):
#     array.reverse()   #tylko tak(bez przypisywani do zmiennych), bo tworzy nową listę o tej samej nazwe, ale z odwróconą kolejnościa fumkcja reverse()
#     return array

# lista=[1,2,3,4,5,6,7]
# print(lista)
# print(swap(lista))


#-------------------------------------------------------------
# Zadanie 26
## Napisz funkcję, która zwraca posortowaną tablicę liczb.


# def sorted(array):
#     array.sort()
#     return array      # tu jest już nowa lista o tej samej nazwie, która powstała w wyniku uzycia funkcji .sort()


# lista = [25,2,3,5,1,20,4]
# print(lista)
# print(sorted(lista))

# # # #rozwiązanie MM
# def sort ( a ):
#     return sorted (a)

# print ( sorted ([ 2 , 1 , 9 ]))

#-------------------------------------------------------------
# Zadanie 27
## Napisz funkcję,, która zwraca listę elementów środkowych.
## makeMiddle([1,2,3,4]) = [2, 3]
## Zakładamy, że długość tablicy jest zawsze podzielna przez 2.

# def makeMiddle(array):
#     lenght = len(array)
#     return (array[lenght//2]-1,array[(lenght//2)])

# print(makeMiddle([1,2,3,4,5,6,7,8,9,10])) 

#-------------------------------------------------------------
# Zadanie 28
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