def wyswietl(num1, num2):
    print(f'Liczba 1: {num1}')
    print(f'Liczba 2: {num2}')

wyswietl(2, 4)

##################### *args #########################
def wyswietlArgs(num1, *args):
    print(f'Liczba 1: {num1}')
    for i in args:
        print(f'Następna wartość: {i}')

wyswietlArgs(1, 222, 332, 31, -75)


imiona = ['Kasia', 'Anna', 'Tomasz']
wyswietlArgs(imiona) #### wyświetli wszystko jeden po drugim
wyswietlArgs(*imiona) ### wyświetli jeden pod drugim


import os
os.system('cls') ### czyszczenie ekranu


#################### **kwargs ################################

def pracownik(**kwargs):
    for key, val in kwargs.items():
        print(f'Klucz {key}, wartość: {val}')

pracownik1 = {
    'imie':'Janusz',
    'nazwisko':'Kowalski',
    'wiek':21,
    'umowaOprace':True
}

pracownik(**pracownik1)
