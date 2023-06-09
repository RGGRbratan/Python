class Ksiazka:
    def __init__(self, id, tytul, autor, wydawca, isbn, rok_wydania, gatunek, liczba_dostepnych_egzemplarzy,
                 liczba_wszystkich_egzemplarzy):
        self.id = id
        self.tytul = tytul
        self.autor = autor
        self.wydawca = wydawca
        self.isbn = isbn
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_dostepnych_egzemplarzy = liczba_dostepnych_egzemplarzy
        self.liczba_wszystkich_egzemplarzy = liczba_wszystkich_egzemplarzy

    def __str__(self):
        return f"id {id}; autor: {self.autor}; tytul: {self.tytul}; wydawca: {self.wydawca}; isbn: {self.isbn};" \
               f" rok_wydania: {self.rok_wydania}; gatunek: {self.gatunek}; " \
               f"liczba_dostepnych_egzemplarzy: {self.liczba_dostepnych_egzemplarzy}; " \
               f"liczba_wszystkich_egzemplarzy: {self.liczba_wszystkich_egzemplarzy};"
