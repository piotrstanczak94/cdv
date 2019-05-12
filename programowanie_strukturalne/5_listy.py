programowanie = ['Python', 'PHP', 'C#', 'JS', 'Java']
print(programowanie)
print(type(programowanie))

first = programowanie[0]
print(f'Pierwszy język programowania w liście: {first}')

last = programowanie[-1]
print(f'Ostatni język programowania w liście: {last}')

## dodanie nowego elementu do listy

programowanie.append('R')
print(programowanie)

# Zliczanie elementów w liście

programowanie.append('Python')
ile = programowanie.count('Python')
print(f'Ilość elementów: {ile}')

iloscElem = len(programowanie)
print(f'Ilość elementów w liście: {iloscElem}')

# połączenie list

print(programowanie)
inneJezyki = ['C', 'C++']
programowanie.extend(inneJezyki)
print(programowanie)
print(inneJezyki)

#wyczyszczenie listy

nowa = programowanie
print(id(programowanie))
print(id(nowa))

nowa.append('GO')
print(nowa)
print(programowanie)

nowa.clear()
print(nowa)
print(programowanie)
