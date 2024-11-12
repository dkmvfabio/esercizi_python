tupla_produzione_agricola = (
    ("Toscana", [
        ("gennaio", ("grano", 1200)),
        ("gennaio", ("mais", 900)),
        ("febbraio", ("grano", 1100)),
        ("febbraio", ("mais", 950)),
        ("marzo", ("grano", 1200)),
        ("marzo", ("mais", 1000)),
        ("aprile", ("grano", 1000)),
        ("aprile", ("mais", 920)),
        ("maggio", ("grano", 980)),
        ("maggio", ("mais", 810)),
        ("giugno", ("grano", 950)),
        ("giugno", ("mais", 740)),
    ]),
    ("Lombardia", [
        ("gennaio", ("grano", 1300)),
        ("gennaio", ("mais", 850)),
        ("febbraio", ("grano", 1250)),
        ("febbraio", ("mais", 920)),
        ("marzo", ("grano", 1200)),
        ("marzo", ("mais", 1000)),
        ("aprile", ("grano", 1100)),
        ("aprile", ("mais", 990)),
        ("maggio", ("grano", 1050)),
        ("maggio", ("mais", 940)),
        ("giugno", ("grano", 1000)),
        ("giugno", ("mais", 830)),
    ]),
    ("Piemonte", [
        ("gennaio", ("grano", 1050)),
        ("gennaio", ("mais", 810)),
        ("febbraio", ("grano", 990)),
        ("febbraio", ("mais", 760)),
        ("marzo", ("grano", 1020)),
        ("marzo", ("mais", 810)),
        ("aprile", ("grano", 1100)),
        ("aprile", ("mais", 900)),
        ("maggio", ("grano", 1170)),
        ("maggio", ("mais", 990)),
        ("giugno", ("grano", 1080)),
        ("giugno", ("mais", 920)),
    ]),
    ("Basilicata", [
        ("gennaio", ("grano", 870)),
        ("gennaio", ("mais", 640)),
        ("febbraio", ("grano", 720)),
        ("febraio", ("mais", 590)),
        ("marzo", ("grano", 810)),
        ("marzo", ("mais", 670)),
        ("aprile", ("grano", 960)),
        ("aprile", ("mais", 790)),
        ("maggio", ("grano", 1010)),
        ("maggio", ("mais", 900)),
        ("giugno", ("grano", 940)),
        ("giugno", ("mais", 820)),
    ]),
)

nomeRegione = str(input("Inserisci il nome di una regione: "))
nomeColtura = str(input("Inserisci il nome di una coltura: "))
while (nomeRegione not in tupla_produzione_agricola or nomeColtura not in tupla_produzione_agricola):
    nomeRegione = str(input("Nome della regione inserito non valido, riprova: "))
    nomeColtura = str(input("Nome della coltura inserito non valido, riprova: "))
        
def analizza_produzione_agricola(tupla_produzione_agricola,nomeRegione, nomeColtura):
    somma = 0
    i = 0
    media_produzione = 0
    max_produzione = []
    mese_max_produzione = []
    produzioneMaggiore = 0
    meseProduzioneMaggiore = 0
    for regione, *dati in tupla_produzione_agricola:
        if (regione==nomeRegione):
            for mese *coltivazioni in dati:
                for coltura, quantita in coltivazioni:
                    if (nomeColtura == coltura):
                        somma += quantita
                        i += 1
                        if (quantita>produzioneMaggiore):
                            produzioneMaggiore = quantita
                            meseProduzioneMaggiore = mese
    media_produzione = somma / i
    for regione, *dati in tupla_produzione_agricola:
        if (regione==nomeRegione):
            for mese, *coltivazioni in dati:
                for coltura, quantita in coltivazioni:
                    if (meseProduzioneMaggiore == mese):
                        mese_max_produzione.append(mese)
                    if (produzioneMaggiore == quantita):
                        max_produzione.append(quantita)

    return media_produzione(max_produzione,mese_max_produzione)

risultato = analizza_produzione_agricola(tupla_produzione_agricola,nomeRegione, nomeColtura)
print(f"Risultato per {nomeRegione} e {nomeColtura}:", risultato)