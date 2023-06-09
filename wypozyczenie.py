from ksiazka import Ksiazka
from pozyczajacy import Pozyczajacy


class Wypozyczenie:

    def __init__(self, id, data_wypozyczenia, data_oddania, ksiazka: Ksiazka, pozyczajacy: Pozyczajacy):
        self.id = id
        self.data_wypozyczenia = data_wypozyczenia
        self.data_oddania = data_oddania
        self.ksiazka = ksiazka
        self.pozyczajacy = pozyczajacy
