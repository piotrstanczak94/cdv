#pętla for

colors = ['red', 'green', 'blue', 'magenta']
print(colors)
print(type(colors))
print() ### Linia przerwy

for color in colors:
    print(color)
print() ### linia przerwy

#text
string = 'CDV - uczelnia ludzi ciekawych'
ilosc = 0
for letter in string:
    print(letter, end=" ")
    if letter != " ":
        ilosc = ilosc + 1
########## zliczanie ilości liter bez znaków spacji #####
print()
print(f'Ilość liter bez spacji: {ilosc}')

## wypisz liczbę z przedziału <1;10>
values = range(1, 11)
for value in values:
    print(value, end=" ")
print()
## wypisz elementy z listy do momentu wartości "end"
list = ['name', 'surname', 'age', 'end', 'city']
for element in list:
    if element == 'end':
        print('Koniec pętli (element ma wartość: end)')
        break
    else:
        print(element, end = " ")
print()

## wypisz liczby parzyste z przedziału podanego przez użytkownika z klawiatury
x = int(input('Podaj x: '))
y = int(input('Podaj y: '))
if y < x:
    z = x
    x = y
    y = z

for i in range(x, y+1):
    if i % 2 == 1:
        continue
    print(i, end=" ")
print()

## pętla while:

i = 1
while i <= 8:
    print(i, end=" ")
    i += 1

## pętla nieskończona
'''
while True:
    print('Pętla nieskończona')
'''
