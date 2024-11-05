datiMensili = (("Milano", [("Gennaio", 170),("Febbraio", 190),("Marzo", 120),("Aprile", 140),
                          ("Maggio", 150),("Giugno", 90),("Luglio", "N/D"),("Agosto", "N/D"),
                          ("Settembre", 220),("Ottobre", 200),("Novembre", 270),("Dicembre", 240)])
               ("Bergamo", [("Gennaio", 230),("Febbraio", 170),("Marzo", 190),("Aprile", 170),
                          ("Maggio", 210),("Giugno", 110),("Luglio", "N/D"),("Agosto", "N/D"),
                          ("Settembre", "N/D"),("Ottobre", 130),("Novembre", 190),("Dicembre", 200)]),

               ("Como", [("Gennaio", 110),("Febbraio", 150),("Marzo", 150),("Aprile", 190),
                          ("Maggio", 130),("Giugno", "N/D"),("Luglio", "N/D"),("Agosto", "N/D"),
                          ("Settembre", 190),("Ottobre", 100),("Novembre", 240),("Dicembre", "N/D")]))

nomeCitta = str(input("Inserisci il nome di una città da analizzare: "))


def analisiDati(nomeCitta, datiMensili):
    meseMax = ""
    meseMin = ""
    valoreMax = 0
    valoreMin = 1000
    media = 0
    somma = 0
    i = 0

    # Media
    for citta, *dati in datiMensili:
        if(nomeCitta == citta):
            for mese, valore in dati:
                if (valore == "N/D"):
                    pass
                else:
                    somma += valore
                    i+=1
    media = somma/i

    # Max
    for citta, *dati in datiMensili:
        if(nomeCitta == citta):
            for mese, valore in dati:
                if (valore == "N/D"):
                    pass
                else:
                    if(valore>valoreMax):
                        meseMax = mese
                        valoreMax = valore

    # Min
    for citta, *dati in datiMensili:
        if(nomeCitta == citta):
            for mese, valore in dati:
                if (valore == "N/D"):
                    pass
                else:
                    if(valore<valoreMin):
                        meseMin = mese
                        valoreMin = valore
    datiAnalizzati = (media,(valoreMax,meseMax),(valoreMin,meseMin))
    
    return print(datiAnalizzati)
ciclo = True
while ciclo:
    nomeCitta = str(input("Inserisci il nome di una città da analizzare: "))
    for citta, *dati in datiMensili:
        if(nomeCitta==citta):
            ciclo = False
            break
        else:
            print("Nome città inserito non valido.")

print(analisiDati(nomeCitta, datiMensili))