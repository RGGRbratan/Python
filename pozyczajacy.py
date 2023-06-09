class Pozyczajacy:
    id_wypozyczen = ()

    def __init__(self, id, imie, nazwisko):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return f"id {id}; imie: {self.imie}; nazwisko: {self.nazwisko};"
