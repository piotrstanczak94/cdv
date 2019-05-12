#zmienne lokalne i globalne


#precyzja liczby
x = "{0:.3f}".format(5)
print(x)

def plnToChf(value):
    kursChf = 3.7800
    iloscChf = value / kursChf
    iloscChf = "{0:.0f}".format(iloscChf)
    return iloscChf

chf = plnToChf(100)
print(chf)

####################################

zmiennaGlobal = 10
print(f'\nZmienna globalna: {zmiennaGlobal}')
print(f'\nId globalna: {id(zmiennaGlobal)}')

def spr():
    global zmiennaGlobal
    zmiennaGlobal = 20
    print(f'\nZmienna globalna wewnątrz funkcji: {zmiennaGlobal}')
    print(f'\nId zmiennej globalnej wewnątrz funckji: {id(zmiennaGlobal)}')

spr()
    print(f'\nZmienna globalna po wyjściu z funkcji: {zmiennaGlobal}')
