#listy
programowanie = ['PHP', 'Python', 'Java']
print(type(programowanie))
programowanie.append('C#')

#tuple
names = ('Anna', 'Janusz')
print(type(names))
first = names[0]

#słowniki
person = {
    'name':'Janusz',
    'city':'Poznań',
    'job':'director',
    'age':30,
    'children':True
    }

print(type(person))
print(person)
print(person['city'])

print(person['xyz']) #błąd

print(person.get('xyz', 'Brak klucza')
print(person.get('job', 'Brak klucza')
