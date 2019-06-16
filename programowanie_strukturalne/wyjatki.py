'''
x = 2
y = 0
wynik = x / y

Błąd. Próba dzielenia przez zero. Wyświetli błąd w konsoli
'''

def iloraz(x, y):
    try:
        result = x / y
        print(f'Wynik dzielenia {x} / {y} wynosi: {result}')
    except ZeroDivisionError:
        print('Dzielenie przez zero!')

iloraz(3, 4)
iloraz(3, 0)

############ zadanie z tablicy ######################
'''Obliczyść wartość (a kwadrat + b) dzielone
przez (a + b) do kwadratu dla zmiennych a i b typu
float wczytywanych z klawiatury. Sprawdzić wykonalność
obliczenia'''

a = float(input('Podaj liczbę a:'))
b = float(input('Podaj liczbę b:'))
def oblicz (a, b):
    try:
        result = ((a*a)+b)/((a+b)*(a+b))
        print(f'Wynik podanego wyrażenia, gdzie a={a} i b={b} wynosi {result}')
    except ZeroDivisionError:
        print('Próba dzielenia przez zero')
oblicz(a, b)

'''Wykorzystując zmienne typu double obliczyć wartość
wyrażenia wynoszącą:
a kwadrat + b dla c > 0
a - b kwadrat dla c < 0
1 / a - b dla c = 0
Sprawdzić wykonalność obliczenia.'''

a = double(input('Podaj liczbę a:'))
b = double(input('Podaj liczbę b:'))
c = double(input('Podaj liczbę c:'))

def wyrazenie(a, b, c):
    try:
        if c > 0:
            result ((a*a) + b)
        elif c < 0:
            result (a - (b*b))
        else c = 0:
            result (1/(a-b))
    except ZeroDivisionError:
        print('Próba dzielenia przez zero')

wyrazenie(a, b, c)
