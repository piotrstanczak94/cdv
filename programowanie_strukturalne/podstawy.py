print("CDV")
print(2)

'''
komentarz
blokowy
'''

# - komentowanie liniowe

'''
#potegowanie
potega = 2 ** 10
print(potega)

#pobieranie danych z klawiatury
imie = input("Podaj imię:")
#konkatenacja +
print("Twoje imię podane z klawiatury: " + imie)
nazwisko = input("Podaj nazwisko: ")
#Twoje imie: ..., Twoje nazwisko: ...
print("Twoje imię: " + imie + ", Twoje nazwisko: " + nazwisko)

print("Podaj swój wiek:", end="")
wiek = input()
print(type(wiek))
print("Twój wiek: " + wiek)

wiek1 = 30
print(type(wiek1)) # jest to int
# print("Twój wiek: " +wiek1) Z plusem wyświetli błąd, prawidłowa wersja:
print("Twój wiek: ", wiek)

nazwisko = "Kowalski"
pierwszyZnak = nazwisko[0]
print(pierwszyZnak)

dlugosc = len(nazwisko)
print(dlugosc)

ostatniZnak = nazwisko[len(nazwisko) -1]
print(ostatniZnak)

ostatniZnak = nazwisko[-1]
print(ostatniZnak)
'''

#konwersja
x = "5"
print(type(x)) #str string

x = int(x)
print(type(x)) #int

y = 4
print(type(y)) #int

y = y / 2
print(type(y)) #float
print(y) #2.0

nazwisko = "Kowalski"
print(nazwisko[0]) #K
print(nazwisko[0:3]) #Kow
print(nazwisko[-2]) #k
print(nazwisko[-2:]) #ki
print(nazwisko[:-2]) #Kowals
print(nazwisko[:-2:2]) #Kwl


