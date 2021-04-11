#-------------------------------------------------------------
# Zadanie 1
## Kostka do gry.
## Napisz program, który losuje liczbę, która może pojawić się na kostce do gry,
## czyli liczbę od 1 do 6.

# import random as r
# print(r.randrange(1,7))

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


##****** inna wersja **********

# word = input('Podaj wyraz\n')
# print(word.endswith('tka'))
