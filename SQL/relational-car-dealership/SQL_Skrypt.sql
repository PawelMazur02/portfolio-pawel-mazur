use [BDN_2023_188965_188950_188972]

CREATE TABLE salon.Samochody (
    ID_Samochodu INT PRIMARY KEY,
    Marka VARCHAR(50),
    Model VARCHAR(50),
    RokProdukcji INT,
    Cena DECIMAL(10, 2)
);


INSERT INTO salon.Samochody VALUES (1, 'Toyota', 'Corolla', 2022, 60000),
                              (2, 'Ford', 'Focus', 2023, 55000),
                              (3, 'BMW', 'X5', 2021, 90000),
                              (4, 'Honda', 'Civic', 2022, 58000),
                              (5, 'Volkswagen', 'Golf', 2023, 52000);


CREATE TABLE pospólstwo.Klienci (
    ID_Klienta INT PRIMARY KEY,
    Imię VARCHAR(50),
    Nazwisko VARCHAR(50),
    Miejscowosc VARCHAR(50),
    Ulica VARCHAR(50),
    NumerTelefonu VARCHAR(9)
);


INSERT INTO pospólstwo.Klienci VALUES (1, 'Jan', 'Kowalski', 'Warszawa', 'Kwiatowa 5', '1234567890'),
                             (2, 'Anna', 'Nowak', 'Kraków', 'Leśna 12', '987654321'),
                             (3, 'Piotr', 'Wiśniewski', 'Gdańsk', 'Słoneczna 8', '111222333'),
                             (4, 'Marta', 'Lewandowska', 'Poznań', 'Ogrodowa 3', '555666777'),
                             (5, 'Paweł', 'Kowalczyk', 'Wrocław', 'Polna 7', '999888777');


CREATE TABLE salon.Zamówienia (
    ID_Zamówienia INT PRIMARY KEY,
    ID_Klienta INT FOREIGN KEY REFERENCES pospólstwo.Klienci(ID_Klienta),
    ID_Samochodu INT FOREIGN KEY REFERENCES salon.Samochody(ID_Samochodu),
    DataZamówienia DATETIME,
    StatusZamówienia VARCHAR(20)
);

INSERT INTO salon.Zamówienia VALUES (1, 1, 2, '2023-01-15 10:30:00', 'Oczekujące'),
                                (2, 3, 4, '2023-02-03 14:45:00', 'Zrealizowane'),
                                (3, 2, 1, '2023-03-08 09:15:00', 'Oczekujące'),
                                (4, 4, 5, '2023-04-20 11:00:00', 'Zrealizowane'),
                                (5, 5, 3, '2023-05-12 16:20:00', 'Oczekujące');


CREATE TABLE pospólstwo.Pracownicy (
	ID_Pracownika INT PRIMARY KEY,
	Imię VARCHAR(50),
	Nazwisko VARCHAR(50),
	Stanowisko VARCHAR(150),
	DataZatrudnienia DATE,
	ZarobkiMiesieczne DECIMAL(10, 2)
);
 

INSERT INTO pospólstwo.Pracownicy VALUES (1, 'Adam', 'Nowak', 'Właściciel, Sprzedawca', '2022-01-10', 10000),
                             	(2,'Maria','Kowalska','Menedżer, Mechanik','2021-05-20', 8000),
                             	(3, 'Michał', 'Wiśniewski', 'Mechanik', '2022-03-15', 6000),
                             	(4, 'Katarzyna', 'Lewandowska', 'Sprzedawca', '2023-02-08', 7000),
                             	(5, 'Wojciech', 'Kowalczyk', 'Sprzedawca' , '2022-09-01', 6500);



CREATE TABLE salon.Serwis (
    ID_Serwisu INT PRIMARY KEY,
    ID_Samochodu INT FOREIGN KEY REFERENCES salon.Samochody(ID_Samochodu),
    ID_Pracownika INT FOREIGN KEY REFERENCES pospólstwo.Pracownicy(ID_Pracownika),
    DataRozpoczęcia DATETIME,
    DataZakończenia DATETIME,
    Koszt DECIMAL(10, 2)
);


INSERT INTO salon.Serwis VALUES (1, 3, 3, '2023-01-20 10:00:00', '2023-01-20 14:30:00', 1200),
                             (2, 2, 5, '2023-02-05 09:30:00', '2023-02-05 12:45:00', 800),
                             (3, 4, 3, '2023-03-12 11:15:00', '2023-03-12 16:00:00', 1500),
                             (4, 1, 2, '2023-04-25 13:45:00', '2023-04-25 17:00:00', 1000),
                             (5, 5, 4, '2023-05-15 08:00:00', '2023-05-15 11:30:00', 900);
