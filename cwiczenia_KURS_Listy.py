#-------------------------------------------------------------
# Zadanie 1
## Napisz program, który wypisuje liczby od 5 do 100, które mają dokładnie 4 dzielniki.

# for i in range ( 5 , 101 ):
#     score = 0
#     for j in range ( 1 ,i+ 1 ):
#         if i %j == 0 :
#             score += 1
#     if score == 4 :
#         print (i)


#-------------------------------------------------------------
# Zadanie 2
## Napisz program, który wypisuje liczby od 10 do 500, oprócz 3, 5, 100, 150. Użyj continue.

# for i in range(10,501):
#     if i == 100 or i == 150:  #bez i == 3 or i == 5 - bo zakres pętli jest od 10
#         continue
#     print(i)


#-------------------------------------------------------------
# Zadanie 3-- sprawdzić!!!!!!
## Napisz program, który sprawdza czy wyraz jest palindromem przy użyciu pętli while.

# ----- sposób 1 -----
# # print("----- sposób 1 -----")
# word = input ( 'Podaj slowo \n ' )
# is_palindrom = True                 #zmienna pomocnicza przyjmuje wartość TRUE
# left = 0                            #ustalamy początkową wartość zmiennej left na 0, aby móc odczytac pierwszą(zerową) literę ciągu
# right = len (word)- 1               #zmienna right przyjmuje wartość odpowiadającą numerowi ostatniej litery ciagu (-1, bo liczymy od zera)
# print(word[left])
# print(word[right])
# while left<right:                  # do chwili gdy pierwsza i ostatnia ( a następnie kolejne druga i przedostatnia itd.) litera ciągu sa takie same wykonuj pętle while, zakończ gdy będą różne 
#     if word[left]!=word[right]:     # sprawdź czy pierwsza i ostatnia litera (i odpowiednio kolejne) są różne
#         is_palindrom = False        # jeżeli tak, to przypisz zmiennej is_palindrom wartość False
#         break                       # i zakończ pętlę
#     left+= 1                        # zmień wartość zmiennej left o 1 - aby sprawdzic następną literę ciągu(od lewej)
#     right-= 1                       # zmień wartość zmiennej right o -1 (w dół) - aby sprawdzic następną literę ciągu(od prawej) i porównać je w pętli while i w ifie
#     print(word[left],"- z lewej")
#     print(word[right],"- z prawej")

# print (is_palindrom)                # wyświetl wartość zmiennej is_palindrom na ekranie w zaleznosci jaka otrzymala ona wartoś


# # # ----- sposób 2 -----
# print("----- sposób 2 -----")
# #word = input ( 'Podaj wyraz \n ' )
# left = 0
# right = len (word)- 1
# is_palindrom = True
# while left<right:
#     if word[left]!=word[right]:
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
# Zadanie 7
## Napisz program, który losuje liczby w Dużym Lotku bez powtórzeń.


# import random as r
# for i in range(6):
#     print(r.randrange(1,50))

##---- sposób 1-----
# import random as r
# numbers =[]
#     #tak długo sie wykonuje az dostaniemy 6 liczb w liscie
# while len(numbers)!=6:
#     number = r.randint(1,49)      #49 bo jest randint
#     if not number in numbers:
#         #jeszcze tej liczby nie wylosowałem to dodaje ja do listy
#         numbers.append(number)
# numbers.sort()
# print(numbers)

# # #---- sposób 2-----
# import random as r
# #definiuje zbiór
# numbers = set()       #   set to zbiór, i nie mogą sie w nim powtarzać elementy
#     #tak długo sie wykonuje az dostaniemy 6 liczb w liscie
# while len(numbers)<6:
#     number = r.randint(1,49)  #randint domyka przedział
#     numbers.add(number)
# print(sorted(numbers))

# numbers ={} # typ dict
# numbers = {1,2,3,4,5} #typ numbers



#-------------------------------------------------------------
# Zadanie 10
## Napisz program, który odczytuje listę i na ekran pokazuję największy element listy.


# numbers = []
# size = int(input("Podaj liczbę elementów: "))
# for i in range(1, size+1):
#     element = int(input("Podaj liczbę " +str(i)+": "))
#     numbers.append(element)
# # lista = [2,4,5,7,9,9,787,4,54478,15,8787,8273897289,4534,151655165]
# print("Najwieksza z liczb, to:",max(numbers))

# # samodzielnie napisane wyznaczanie maksuimum
# max = numbers[0] # zakładam że maksem jest element zerowy
# for value in numbers:
#     # jeżeli element jest większy od max, to staje sie maksem
#     if value > max:
#         max = value
# print("Najwieksza z liczb, to:",max)


#-------------------------------------------------------------
# Zadanie 11
## Napisz program wczytujący listę i wypisującą listę w posortowany sposób.

# numbers = []
# size = int(input("Podaj liczbę elementów: "))
# for i in range(1, size+1):
#     element = int(input("Podaj liczbę " +str(i)+": "))
#     numbers.append(element)
# print("Liczba elementów listy to:",len(numbers))
# print("Lista składa sie z nastęujących elementów:",numbers)
# numbers.sort() # nie może być w print
# print("Posortowane elementy listy:",numbers)

#-------------------------------------------------------------
# Zadanie 12
# Napisz program, który odczytuje listę i liczby całkowite listy.
# Na ekran pokazuję liczby parzyste listy.

# numbers = []
# size =int(input("Podaj liczbę elementów: "))
# for i in range(1, size+1):
#     element = int(input("Podaj liczbę " +str(i)+": "))
#     numbers.append(element)
# even = []
# for value in numbers:8
#    if value%2 == 0:
#         even.append(value)
# even.sort()
# print("Liczba elementów parzystych to: ",len(even))
# print("Elementy parzyste listy to:",even)
# numbers.sort()
# print("Liczba elementów listy to:",len(numbers))
# print("Lista składa sie z nastęujących elementów:",numbers)



#-------------------------------------------------------------
# Zadanie 13
## Napisz program, który odczytuje listę i na ekran pokazuję co drugi element listy.

# numbers = []
# size = int(input("Podaj liczbę elementów: "))
# for i in range(1, size+1):
#     element = int(input("Podaj liczbę " +str(i)+": "))
#     numbers.append(element)
# ## ----- spodób 1 ------------
# print("-----Sposób 1-----")
# for index,value in enumerate (numbers):
#      if index% 2 == 1 :     #gdy z dzielenia zostaj 1 to jest to co druga liczba
#          print (value,end=" ")
         
# ## ----- spodób 2 ------------
# print("\n-----Sposób 2-----")
# everySecond = []
# for index,value in enumerate (numbers):
#     if index%2 == 1:
#         everySecond.append(value)
# print("Co drugi element listy, to:",everySecond)

#-------------------------------------------------------------
# Zadanie 14
## Narysuj wykres funkcji 2x+1 na przedziale <-5,5>

# alternatywne wersje importu biblioteki matplotlib
# import matplotlib.pyplot as p
# import numpy


# import pylab as p
# x = range(-5,6)
# y = []
# for i in x:
#     y.append(2*i+1)
# p.plot(x,y,color='red')
# p.title('Wykres y=2x+1')
# p.scatter(x,y)
# p.grid()
# p.show()


## dłuższy sposób
# import pylab as p
# x = []
# for i in range(-5,6):
#     x.append(i)
# y=[]
# for value in x:
#     y.append(2*value+1)
# p.plot(x,y,color='red')
# p.title('Wykres y=2x+1')
# p.scatter(x,y)
# p.grid()
# p.show()



## ponizej przykład z wykładu
# x = [1,2,3]
# y = [2,3,4]
# p.plot(x,y)
# p.show()
#-------------------------------------------------------------
# Zadanie 15
## Narysuj wykres funkcji 3x+15 na przedziale <-10,15>

# import pylab
# x = range(-10,16) # zamiast robić listę, podajemy zakres zmiennej
# ##print(list(x)) # wyświetla zakre range
# y = []
# for i in x:
#     y.append(3*i+15)
# pylab.plot(x,y)
# pylab.title('Wykres y=3x+15')
# pylab.scatter(x,y)
# pylab.grid()
# pylab.show()


#-------------------------------------------------------------
# Zadanie 16
## Narysuj wykres funkcji x*x, na przedziale <5,15>

# import pylab
# x = range(5,16)
# y = []
# for i in x:
#     y.append(i*i)
# pylab.plot(x,y)
# pylab.title('Wykres y=x*x')
# pylab.scatter(x,y)
# pylab.grid()
# pylab.show()


#-------------------------------------------------------------
# Zadanie 17
## Rozwiąż przykładowe zadanie na serwisie Codility:
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
#     print("Lista utworzona:",list)
#     list.sort()
#     print("Lista uposortowana:",list)
#     list.reverse()
#     print("Lista odwrócona:",list)
#     print("Maksimum listy, to:",max(list))
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
#         #print("The smallest positive integer (greater than 0) that does not occur in A, is:",k,".")
#         return k      
#     pass   


# #listy do testowania
# #a=[-145,-258,-654,-55,-2,-548,-3,-555,-255]
# #a=[-145,-258,-654,-55,-2,-548,-3,-555,-255,1]
# #a=[1_000_001,50,-3,56,23,-2,3,9,55,-23,67,12,-11,345,1,0,2,4,5,6,7,8,10,11,12,13,14]
# #a=[-48752,50,-3,56,7,23,15,-2,3,9,55,-23,67,12,0,-11,345,2,5,6,4,8,10,12,1,13,14]
# #a=[1,2,57,9,45,7,23,8,962,4,5,3]
# #a=[1, 3, 6, 4, 1, 2]
# #a=[1, 2, 3]
# #a=[-1,-3]

# print("The smallest positive integer (greater than 0) that does not occur in A, is:",solution(a),".")






# #-------------------------------------------------------------
# Zadanie 18
## Napisz program odczytujący dane z pliku.
## Przykładowe dane w pliku:
## Ala ma kota
## Lubię programować
## Na ekran wypisz występowanie poszczególnych liter.


# file = open("E:\Programowanie\Python\KURS\kurs_odczyt.txt","r",encoding="utf-8")
# if file.mode == "r":
#     contents = file.read()
#     print (contents)
# for i in range (0,450):
#     znak = chr(i)
#     if znak in contents:
#         print(znak,"- występuje",contents.count(znak),"razy")
# file.close()
