class Ksiazka:
    def __init__(self, tytul, autor, liczba_stron):
        self.tytul = tytul
        self.autor = autor
        self.liczba_stron = liczba_stron

    def opis(self):
        return f"{self.tytul} - {self.autor}, {self.liczba_stron}"
    

ksiazka = Ksiazka("Silmarillion", "J. R. R. Tolkien", 560)

print(ksiazka.autor)
print(ksiazka.opis())