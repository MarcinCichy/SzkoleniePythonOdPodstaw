# Mamy duza liczbe argumentow funkcji
# latwo o bledy w kolejnosci
# ROZWIAZANIE 1
def hi(first_name,last_name):
    print(first_name,last_name)
    # ta funkcja nic nie zwraca, zwraca None
hi(last_name='Makaruk',first_name='Michal')
hi('Makaruk','Michal') # zle wpisane dane
# ROZWIAZANIE 2
# **- specjalne oznaczenie
def hello(**arguments):
    # arguments zamieniony jest na dictionary, dict
    print(type(arguments))
    print(arguments['name'])
    print(arguments['surname'])
hello(name='Michal',surname='Makaruk')
hello(**{'surname': 'Makaruk','name': 'Michal'})
# ROZWIAZANIE 3
def bye(names):
    if 'name' in names:
        print(names['name'])
    if 'surname' in names:
        print(names['surname'])
bye({'name': 'Piotr', 'surname': 'Kowalski'})
bye({'name': 'Jan'})
bye({'surname': 'Kowalski'})
# ROZWIAZANIE 4
# *args - lista
def bye_bye(*args):
    for i in args:
        print(i)
bye_bye(1,2,5,10) # [1,2,5,10] -> (1,2,5,10)
bye_bye(2,5)
bye_bye(12,12,55,21,210,120,210,500) # liczba argumentow moze byc rozna

