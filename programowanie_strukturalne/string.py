tekst = "Anna, paweł, julIA"

lista = tekst.split(", ")
print(tekst)
print(linia)
print(type(lista))

imie1 = lista[0]
print(imie1)

imieDuze = imie1.upper()
print(imieDuze)

imieMale = imie.lower()
print(imieMale)

#sprawdzenie zawartosci
print("\nPodaj swoje nazwisko: ", end="")
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc) #True lub False

text1 = "\nJulia\n"
text2 = "Nowak"
print(text1 + text2)

text1 = text1.rstrip()
print(text1 + text2)

text = "%s, Java i %s" % ("PHP", "Python")
print(text)
