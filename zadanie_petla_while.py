imie2 = 'Ala'
ile = 4
licznik = 0
zwierze = 'kot'
while licznik < ile :
    print("{0} ma {1} {2}y".format(imie2, str(licznik+1),zwierze))
    licznik +=1

szukane_slowo = "Al"

warunek = imie2.startswith(szukane_slowo)
if warunek:
    print(imie2 + ' Zaczyna sie od: '+ szukane_slowo)
else:
    print(imie2 + 'Nie zaczyna sie od: '+ szukane_slowo)
