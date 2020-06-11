# Zadanie 11
## Napisz funkcję, która odczytuje jako argument liczbę i wypisuje liczbę dzielników.

def numbers_of_dividers(number):
    score = 0
    for i in range(1,number+1):
        if number%i == 0:
            score += 1
    return score

# number = int(input("Podaj liczbę: "))
# result = numbers_of_dividres(number)
# print("Ilość dzielników liczby ",number,", wynosi:",result)