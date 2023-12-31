from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Summa():
    def __init__(self, logiikka, syote) -> None:
        self.logiikka = logiikka
        self.syote = syote

    def suorita(self):
        self.logiikka.plus(int(self.syote))

class Erotus():
    def __init__(self, logiikka, syote) -> None:
        self.logiikka = logiikka
        self.syote = syote

    def suorita(self):
        self.logiikka.miinus(int(self.syote))

class Nollaus():
    def __init__(self, logiikka) -> None:
        self.logiikka = logiikka

    def suorita(self):
        self.logiikka.nollaa()


class Kumoa():
    def __init__(self, logiikka, prior) -> None:
        self.logiikka = logiikka
        self.prior = prior

    def suorita(self):
        self.logiikka.aseta_arvo(self.prior)



class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self._syote_kentta = ttk.Entry(master=self._root)
        self._edellinen = 0

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        return self._syote_kentta.get()

    def _suorita_komento(self, komento):
        self._komennot = {
            Komento.SUMMA: Summa(self._sovelluslogiikka, self._lue_syote()),
            Komento.EROTUS: Erotus(self._sovelluslogiikka, self._lue_syote()),
            Komento.NOLLAUS: Nollaus(self._sovelluslogiikka),
            Komento.KUMOA: Kumoa(self._sovelluslogiikka, self._edellinen)
        }

        komento_olio = self._komennot[komento]
        self._edellinen = [self._sovelluslogiikka.arvo()]
        komento_olio.suorita()
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())
