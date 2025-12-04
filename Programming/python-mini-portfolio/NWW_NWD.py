liczba1=int(input("Podaj pierwszą liczbę: "))
liczba2=int(input("Podaj drugą liczbę: "))
pomocnicza=liczba1*liczba2
licznik=0
while liczba2>0:
    licznik+=1 
    reszta=liczba1%liczba2 
    liczba1=liczba2 
    liczba2=reszta
print("Pętla wykonana {} razy".format(licznik))
print("Największy wspólny dzielnik to:",liczba1)
nwd=liczba1
nww=pomocnicza/nwd
print("Największa wspólna wielokrotność to:",int (nww))
