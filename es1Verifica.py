tupla_partite = (
    ("GiocatoreA", "GiocatoreB", 3, 2),
    ("GiocatoreC", "GiocatoreD", 2, 3),
    ("GiocatoreB", "GiocatoreC", 3, 0),
    ("GiocatoreA", "GiocatoreD", 3, 1),
    ("GiocatoreB", "GiocatoreD", 2, 3),
)

def media_set_partita(tupla_partite):
    media = 0
    somma = 0
    i = 0
    for giocatore1, giocatore2, set1, set2 in tupla_partite:
        somma += set1 + set2
        i += 2
    media = somma/i
    return media

def media_set_giocatore(tupla_partite,giocatore):
    media = 0
    somma=0
    i=0
    for giocatore1 , giocatore2, set1, set2 in tupla_partite:
        if giocatore1 == giocatore:
            if set1>set2:
                somma+=set1
                i+=1
        elif giocatore2 == giocatore:
            if set2>set1:
                somma+=set2
                i+=1
            
    if(i==0):
        return f"Il giocatore '{giocatore}' non esiste o non ha vinto alcun set."
    else:
        media = somma/i
        return media
    
def match_piu_combattuto(tupla_partite):
    match_piu_combattuti = []
    max = 0

    for giocatore1, giocatore2, set1, set2 in tupla_partite:
        somma = set1 + set2
        if (somma > max):
            max = somma

    for giocatore1, giocatore2, set1, set2 in tupla_partite:
        somma = set1 + set2
        if (max == somma):
            match_piu_combattuti.append(giocatore1)
            match_piu_combattuti.append(giocatore2)
            match_piu_combattuti.append(set1)
            match_piu_combattuti.append(set2)
    return f"Il/I match più combattito/i sono: {match_piu_combattuti}, con un punteggio massimo di {max}"

def match_meno_combattuto(tupla_partite):
    match_piu_combattuti = []
    min = float('inf')

    for giocatore1, giocatore2, set1, set2 in tupla_partite:
        somma = set1 + set2
        if (somma < min):
            min = somma

    for giocatore1, giocatore2, set1, set2 in tupla_partite:
        somma = set1 + set2
        if (min == somma):
            match_piu_combattuti.append(giocatore1)
            match_piu_combattuti.append(giocatore2)
            match_piu_combattuti.append(set1)
            match_piu_combattuti.append(set2)
    return f"Il/I match meno combattito/i sono: {match_piu_combattuti}, con un punteggio minimo di {min}"

def percentuale_vittorie_giocatore(tupla_partite,giocatore):
    tot = 0
    i = 0
    for giocatore1 , giocatore2, set1, set2 in tupla_partite:
        if giocatore1 == giocatore:
            if set1>set2:
                tot += 1
        elif giocatore2 == giocatore:
            if set2>set1:
                tot += 1
        i+=1
    if tot==0:
        return "Il giocatore specificato non è valido o non ha vinto alcuna partita."
    else:
        percentuale = (tot*100)/i   
        return f"La percentuale di partite vinte dal giocatore '{giocatore}' equivale al {percentuale}%. " 
    
while True:
    print("[1] Per mostare la media dei set per il numero totale di partite;")
    print("[2] Per mostrare la media dei set vinti di un giocatore a scelta;")
    print("[3] Per mostrare il match più combattuto;")
    print("[4] Per mostrare il match meno combattuto;")
    print("[5] Per mostrare la percentuale di vittore di un giocatore;")
    print("[0] Per terminare.")
    scelta = int(input("Inserisci la scelta desiderata: "))

    if (scelta==1):
        print("Media dei set per totale partite: ")
        print(media_set_partita(tupla_partite))
    elif (scelta==2):
        giocatore = str(input("Inserisci il nome di un giocatore: "))
        print(f"La media del giocatore '{giocatore}' equivale a: ")
        print(media_set_giocatore(tupla_partite,giocatore))
    elif (scelta==3):
        print(match_piu_combattuto(tupla_partite))
    elif (scelta==4):
        print(match_meno_combattuto(tupla_partite))
    elif (scelta==5):
        giocatore = str(input("Inserisci il nome di un giocatore: "))
        print(percentuale_vittorie_giocatore(tupla_partite,giocatore))
    elif (scelta==0):
        break
    elif (scelta<0 or scelta>5):
        print("Scelta inserita non valida.")
