import datetime
import uuid
from datetime import date

from ksiazka import Ksiazka
from pozyczajacy import Pozyczajacy
from wypozyczenie import Wypozyczenie


class Biblioteka:
    spis_ksiazek = {}
    spis_wypozyczajacych = {}
    spis_wypozyczen = {}

    def pokaz_wszystkie_ksiazki(self):
        for id, ksiazka in self.spis_ksiazek.items():
            print(str(ksiazka))

    def pokaz_wszystkie_wypozyczone_ksiazki(self):
        for id, wypozyczenie in self.spis_wypozyczen.items():
            print(f"{str(wypozyczenie.ksiazka)} wypozyczona przez {str(wypozyczenie.pozyczajacy)}")

    def wypozycz_ksiazke(self, ksiazka: Ksiazka, pozyczajacy: Pozyczajacy):
        wypozyczenie_id = uuid.uuid4()
        self.spis_wypozyczen[wypozyczenie_id] = Wypozyczenie(wypozyczenie_id, date.today(),
                                                             datetime.datetime.today() + datetime.timedelta(days=30),
                                                             ksiazka, pozyczajacy)
        print(f"{str(ksiazka)} zostala wypozyczona przez {str(pozyczajacy)}")

    def oddaj_ksiazke(self, ksiazka: Ksiazka, pozyczajacy: Pozyczajacy):
        szukane_ksiazki = []
        for id, wypozyczenie in self.spis_wypozyczen.items():
            if wypozyczenie.ksiazka.id == ksiazka.id and wypozyczenie.pozyczajacy.id == pozyczajacy.id:
                print(
                    f"Pozyczajacy {pozyczajacy.imie} {pozyczajacy.nazwisko} oddal ksiazke {ksiazka.tytul} - {ksiazka.autor}")
                if date.today() > wypozyczenie.data_oddania:
                    f"Ksiazka oddana po terminie"
                self.spis_wypozyczen.pop(id)
        return szukane_ksiazki

    def dodaj_ksiazke(self, tytul, autor, wydawca, isbn, rok_wydania, gatunek, liczba_wszystkich_egzemplarzy):
        ksiazka = Ksiazka(uuid.uuid4(), tytul, autor, wydawca, isbn, rok_wydania, gatunek,
                          liczba_wszystkich_egzemplarzy, liczba_wszystkich_egzemplarzy)
        self.spis_ksiazek[ksiazka.id] = ksiazka
        print(f"{str(ksiazka)} zostala dodana do spisu")

    def edytuj_ksiazke(self, ksiazka: Ksiazka):
        self.spis_ksiazek[ksiazka.id] = ksiazka
        print(f"{str(ksiazka)} zostala edytowana")

    def usun_ksiazke(self, ksiazka: Ksiazka):
        self.spis_ksiazek.pop(ksiazka.id)
        print(f"{str(ksiazka)} zostala usunieta ze spisu")

    def szukaj_ksiazke_autor(self, szukana_fraza):
        szukane_ksiazki = []
        for id, ksiazka in self.spis_ksiazek.items():
            if szukana_fraza in ksiazka.autor:
                szukane_ksiazki.append(ksiazka)
        return szukane_ksiazki

    def szukaj_ksiazke_tytul(self, szukana_fraza):
        szukane_ksiazki = []
        for id, ksiazka in self.spis_ksiazek.items():
            if szukana_fraza in ksiazka.tytul:
                szukane_ksiazki.append(ksiazka)
        return szukane_ksiazki

    def szukaj_ksiazke_gatunek(self, szukana_fraza):
        szukane_ksiazki = []
        for id, ksiazka in self.spis_ksiazek.items():
            if szukana_fraza in ksiazka.gatunek:
                szukane_ksiazki.append(ksiazka)
        return szukane_ksiazki
