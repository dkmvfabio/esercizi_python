# -*- coding: utf-8 -*-
"""07_Verifica_Oggetti_FILA_B_ns.ipynb
**ESERCIZIO 2 : BIBLIOTECA E LIBRI**

Creare la classe `Biblioteca` per contenere una serie di oggetti `Libro`.

La classe `Biblioteca` deve contenere:

* un attributo che rappresenti una lista di libri presenti;
* un metodo per aggiungere un libro alla biblioteca;
* un metodo per rimuovere un libro (dato il codice ISBN);
* un metodo per visualizzare l’elenco dei libri disponibili;
* un metodo per cercare un libro dato il codice ISBN e restituire le sue informazioni.
"""

class Libro:
    def __init__(self, isbn, titolo, autore, anno):
        # Inizializza gli attributi del libro
        self.isbn = isbn
        self.titolo = titolo
        self.autore = autore
        self.anno = anno

    def __str__(self):
        # Restituisce una descrizione leggibile del libro
        return f"{self.titolo} di {self.autore} ({self.anno}) - ISBN {self.isbn} \n"


class Biblioteca:
    def __init__(self):
        # Inizializza la lista dei libri
        self.listaLibri = []

    def aggiungi_libro(self, libro):
        # Aggiunge un libro alla lista
        self.listaLibri.append(libro)

    def cerca_libro(self, sceltaIsbn):
        # Rimuove un libro in base all'ISBN
        if (len(self.listaLibri)) == 0:
            return "Non è presente alcun libro nella lista!"
        for i in range(self.listaLibri):
            for isbn, titolo, autore, anno in (self.listaLibri[i]):
                if self.listaLibri[i].isbn == sceltaIsbn:
                    return self.listaLibri[i]
        return "Il libro cercato non esiste"

    def rimuovi_libro(self, sceltaIsbn):
        # Rimuove un libro in base all'ISBN
        if (len(self.listaLibri)) == 0:
            return "Non è presente alcun libro nella lista!"
        for i in range(self.listaLibri):
            for isbn, titolo, autore, anno in (self.listaLibri[i]):
                if self.listaLibri[i].isbn == sceltaIsbn:
                    self.listaLibri.remove(self.listaLibri[i])
        return "Il libro cercato non esiste"


    def elenco_libri(self):
        # Restituisce la lista dei libri nella biblioteca
        risultato = ""
        print("Lista libri: ")
        for i in range(self.listaLibri):
            risultato += self.listaLibri[i]
        return risultato


while True:
    gestioneBiblioteca = Biblioteca()
    print("Menù:")
    print("[1] Aggiunta libro;")
    print("[2] Cerca libro;")
    print("[3] Rimuovi libro;")
    print("[4] Mostra elenco libri;")
    print("[0] Termina;")
    scelta=int(input("Inserisci la scelta desiderata: "))
    if (scelta == 1):
        titolo = str(input("Inserisci il titolo del libro: "))
        autore = str(input("Inserisci il nome dell'autore: "))
        anno = int(input("Inserisci l'anno di produzione: "))
        while (anno<=0):
            anno = int(input("L'anno inserito non è valido, riprova: "))
        isbn = int(input("Inserisci il codice ISBN: "))
        libro = Libro(isbn,titolo,autore,anno)
        gestioneBiblioteca.aggiungi_libro(libro)
        print("Libro aggiunto.")
    elif (scelta==2):
        sceltaIsbn = int(input("Inserisci il codice ISBN del libro da cercare: "))
        gestioneBiblioteca.cerca_libro(sceltaIsbn)
    elif (scelta==3):
        sceltaIsbn = int(input("Inserisci il codice ISBN del libro da eliminare: "))
        gestioneBiblioteca.rimuovi_libro(sceltaIsbn)       
    elif (scelta == 4):
        gestioneBiblioteca.elenco_libri()
    elif (scelta==0):
        print("Termina.")
        break
    elif (scelta<0 or scelta>4):
        print("Scelta inserita non valida.")

