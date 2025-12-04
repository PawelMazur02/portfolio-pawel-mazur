import random
import statistics

class Student:
    def __init__(self, imie, index):
        self._imie = imie
        self._index = index

    @property
    def name(self):
        return self._imie

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, new_index):
        self._index = new_index

    def info(self):
        print(f"Student: {self._imie}, Numer indeksu: {self._index.numer}, Średnia: {self._index.srednia}")

class Index:
    def __init__(self, numer, srednia):
        self._numer = numer
        self._srednia = srednia

    @property
    def numer(self):
        return self._numer

    @numer.setter
    def numer(self, new_numer):
        self._numer = new_numer

    @property
    def srednia(self):
        return self._srednia

    @srednia.setter
    def srednia(self, new_srednia):
        self._srednia = new_srednia
        
imiona = ["Anna", "Jan", "Maria", "Piotr", "Alicja", "Krzysztof", "Zofia", "Tomasz", "Magdalena", "Adam"]

def generuj_studentow(liczba_studentow):
    students = []
    for i in range(liczba_studentow):
        sr = round(random.uniform(2.0, 5.0), 2)
        
        index_numer = f"{100000+i}"
        
        indeks = Index(numer=index_numer, srednia=sr)
        student_imie = imiona[i]
        students.append(Student(imie=student_imie, index=indeks))
    return students


def statystyka(studenci):
    srednie = [student.index.srednia for student in studenci]
    
    srednia = statistics.mean(srednie)
    dominanta = statistics.mode(srednie)
    mediana = statistics.median(srednie)
    odchylenie_standardowe = statistics.stdev(srednie) 
    
    return srednia, dominanta, mediana, odchylenie_standardowe

ilosc_studentow = 10
studenci = generuj_studentow(ilosc_studentow)

wyniki_statystyki = statystyka(studenci)

print("Lista studentów:")
for student in studenci:
    student.info()

print("\nStatystyki:")
print("Średnia:", wyniki_statystyki[0])
print("Dominanta:", wyniki_statystyki[1])
print("Mediana:", wyniki_statystyki[2])
print("Odchylenie standardowe:", wyniki_statystyki[3])
