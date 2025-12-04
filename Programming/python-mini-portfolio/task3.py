class Indeks:
    def __init__(self, numer_indeksu, srednia):
        self.__numer_indeksu = numer_indeksu
        self.__srednia = srednia

    @property
    def numer_indeksu(self):
        return self.__numer_indeksu

    @numer_indeksu.setter
    def numer_indeksu(self, nowy_numer):
        self.__numer_indeksu = nowy_numer

    @property
    def srednia(self):
        return self.__srednia

    @srednia.setter
    def srednia(self, nowa_srednia):
        self.__srednia = nowa_srednia

class Student:
    def __init__(self, imie, indeks):
        self.__imie = imie
        self.__indeks = indeks

    @property
    def imie(self):
        return self.__imie

    @imie.setter
    def imie(self, nowe_imie):
        self.__imie = nowe_imie

    @property
    def indeks(self):
        return self.__indeks

    @indeks.setter
    def indeks(self, nowy_indeks):
        self.__indeks = nowy_indeks

    def info(self):
        print(f"{self.__imie} - Numer indeksu: {self.__indeks.numer_indeksu} - Średnia: {self.__indeks.srednia}")

indeks1 = Indeks("123456", 5.0)
indeks2 = Indeks("654321", 3.0)

student1 = Student("Paweł", indeks1)
student2 = Student("Paula", indeks2)

student1.info()
student2.info()

#%%
student1.indeks, student2.indeks = student2.indeks, student1.indeks

student1.info()
student2.info()