def witaj():
    print('Witaj', end=' ')
    print('Janusz')

witaj()

def wyswietlWiek(wiek):
    print(f'Twój wiek: {wiek}')

wyswietlWiek(20)

'''
Zadanie po przerwie:
Utwórz funkcję zwracającą  iloczyn dwóch liczb.
Użytkownik podaje dane z klawiatury
'''
def iloczyn(a, b):
    return a * b

a = float(input('Podaj wartość a: '))
b = float(input('Podaj wartość b: '))

print('Iloczyn a oraz b wynosi: ', iloczyn(a, b))

#########################################

def iloraz(a, b):
    return a / b

print('Iloraz wynosi: ', iloraz(2, 4))
print('Iloraz wynosi: ', iloraz(b=2, a=4))
