#Dati dei corsi organizzati in diverse citta
corsi = (
    ("Milano", [
        ("gennaio", ("online", 50)),
        ("gennaio", ("in presenza", 30)),
        ("febbraio", ("online", 40)),
        ("febbraio", ("in presenza", 25)),
        ("marzo", ("online", 50)),
        ("marzo", ("in presenza", 20)),
        ("aprile", ("online", 10)),
        ("aprile", ("in presenza", 15)),
        ("maggio", ("online", 50)),
        ("maggio", ("in presenza", 10)),
        ("giugno", ("online", 30)),
        ("giugno", ("in presenza", 30)),
    ]),
    ("Bologna", [
        ("gennaio", ("online", 45)),
        ("gennaio", ("in presenza", 20)),
        ("febbraio", ("online", 35)),
        ("febbraio", ("in presenza", 30)),
        ("marzo", ("online", 40)),
        ("marzo", ("in presenza", 20)),
        ("aprile", ("online", 45)),
        ("aprile", ("in presenza", 15)),
        ("maggio", ("online", 20)),
        ("maggio", ("in presenza", 25)),
        ("giugno", ("online", 45)),
        ("giugno", ("in presenza", 15)),
    ]),
    ("Roma", [
        ("gennaio", ("online", 60)),
        ("gennaio", ("in presenza", 20)),
        ("febbraio", ("online", 35)),
        ("febbraio", ("in presenza", 30)),
        ("marzo", ("online", 35)),
        ("marzo", ("in presenza", 15)),
        ("aprile", ("online", 20)),
        ("aprile", ("in presenza", 25)),
        ("maggio", ("online", 60)),
        ("maggio", ("in presenza", 25)),
        ("giugno", ("online", 60)),
        ("giugno", ("in presenza", 15)),
    ]), 
    ("Napoli", [
        ("gennaio", ("online", 10)),
        ("gennaio", ("in presenza", 30)),
        ("febbraio", ("online", 40)),
        ("febbraio", ("in presenza", 35)),
        ("marzo", ("online", 15)),
        ("marzo", ("in presenza", 25)),
        ("aprile", ("online", 10)),
        ("aprile", ("in presenza", 35)),
        ("maggio", ("online", 40)),
        ("maggio", ("in presenza", 20)),
        ("giugno", ("online", 40)),
        ("giugno", ("in presenza", 15)),
    ]),     
)

sceltaCitta = str(input("Inserisci il nome della città: "))
sceltaModalita = str(input("Inserisci la modalità del corso: "))

def analizza_partecipanti(corsi,sceltaCitta,sceltaModalita):
    media_partecipanti = 0
    max_partecipanti = 0
    mese_max_partecipanti = []
    somma = 0
    i = 0
    for citta, dati in corsi:
        if citta == sceltaCitta:
            for mese, *corso in dati:
                for modalita, partecipanti in corso:
                    if modalita == sceltaModalita:
                        somma += partecipanti
                        i+=1
                        if partecipanti>max_partecipanti:
                            max_partecipanti=partecipanti

    for citta, dati in corsi:
        if citta == sceltaCitta:
            for mese, *corso in dati:
                for modalita, partecipanti in corso:
                    if modalita == sceltaModalita:
                        if max_partecipanti==partecipanti:
                            mese_max_partecipanti.append(mese)

    if i==0:
        return "La citta o modalità corso inserita non è valida."
    else:
        media_partecipanti = somma/i
        print(f"Il risultato per la città {sceltaCitta} e corso {sceltaModalita}: ")
        return (media_partecipanti,(max_partecipanti, mese_max_partecipanti))

print(analizza_partecipanti(corsi,sceltaCitta,sceltaModalita))


