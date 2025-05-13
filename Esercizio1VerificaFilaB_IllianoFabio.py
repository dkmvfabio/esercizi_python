# -*- coding: utf-8 -*-
"""07_Verifica_Oggetti_FILA_B_ns.ipynb
**ESERCIZIO 1 : PAGELLE**
"""
import math

class Pagella:
    def __init__(self,voti):
        self.voti = voti

    def __repr__(self):
        risultato = ""
        for i in range(len(self.voti)):
            risultato += f"Voto {i+1}: {self.voti[i]}.\n "
        return risultato

    def media(self):
        if len(self.voti) == 0:
            return f"Non ci sono voti in pagella!"
        somma = 0
        n = 0
        for i in range(len(self.voti)):
            somma += self.voti[i]
            n += 1
        media = somma/n
        return f"La media dei voti equivale a {media}."

    def __getitem__(self,indice):
        if len(self.voti) < indice:
            return "Indice non valido!"
        for i in range(len(self.voti)):
            if (indice == i):
                return self.voti[i]
    
    def __eq__(self,pagella):
        if len(self.voti)!=(len(pagella.voti)):
            print("Le pagelle hanno un numero diverso di materie e non possono essere confrontate.")
            return None
        uguali = 0
        for i in range(len(self.voti)):
            if (self.voti[i]) == pagella.voti[i]:
                uguali+=1
        if uguali == len(self.voti):
            return True
        else:
            return False
    
    def __sub__(self,pagella):
        if len(self.voti)!=(len(pagella.voti)):
            print("Le pagelle hanno un numero diverso di materie e non possono essere confrontate.")
            return None
        sottrazioni = []
        for i,j in zip(self.voti,pagella.voti):
            sottrazioni.append(i-j)
        return sottrazioni

    def impegno(self):
        if len(self.voti) == 0:
            return f"Non ci sono voti in pagella!"
        moltiplicazioni = []
        risultato = 0
        for i in range(len(self.voti)):
           moltiplicazioni.append(self.voti[i]*self.voti[i])
        for x in range(len(moltiplicazioni)):
            risultato += moltiplicazioni[x]
        return math.sqrt(risultato)

pagella = Pagella([4,8,6])
print(pagella)
print(pagella[0])
pagella2 = Pagella([2,4,3])
print("Uguaglianza: ", pagella == pagella2)
print("Sottrazione: ", pagella-pagella2)
print("Media pagella 1: ", pagella.media())
print("Impegno: ", pagella.impegno())
