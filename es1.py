tupla_competizioni = (
    ("ChefA", "Piatto1", 8.5, 5),
    ("ChefB", "Piatto2", 7.2, 4),
    ("ChefC", "Piatto3", 9.0, 6),
    ("ChefA", "Piatto4", 7.8, 5),
    ("ChefB", "Piatto5", 8.1, 4),
)

def media_punteggio_competizioni(tupla_competizioni):
    somma = 0
    i = 0
    media = 0
    for nomeChef, piatto, punteggio, giudici in tupla_competizioni:
        somma += punteggio
        i+=1
    media = somma/i
    return media

def media_punteggio_chef(tupla_competizioni, chef):
    somma = 0
    i = 0
    mediaChef = 0
    for nomeChef, piatto, punteggio, giudici in tupla_competizioni:
        if (chef == nomeChef):
            somma += punteggio
            i+=1
    mediaChef = somma/i
    return mediaChef

def competizione_con_piu_giudici(tupla_competizioni):
    numeroMaggioreGiudici = 0
    competizioneMaggiore = [(""),(""),0,0]
    for nomeChef, piatto, punteggio, giudici in tupla_competizioni:
        if(giudici>numeroMaggioreGiudici):
            numeroMaggioreGiudici = giudici
    for nomeChef, piatto, punteggio, giudici in tupla_competizioni:
        if (numeroMaggioreGiudici == giudici):
            competizioneMaggiore[0] = nomeChef
            competizioneMaggiore[1] = piatto
            competizioneMaggiore[2] = punteggio
            competizioneMaggiore[3] = giudici
    return competizioneMaggiore

def competizione_con_meno_giudici(tupla_competizioni):
    numeroMinoreGiudici = 1000
    competizioneMinore = [(""),(""),0,0]
    for nomeChef, piatto, punteggio, giudici in tupla_competizioni:
        if(giudici<numeroMinoreGiudici):
            numeroMinoreGiudici = giudici
    for nomeChef, piatto, punteggio, giudici in tupla_competizioni:
        if (numeroMinoreGiudici == giudici):
            competizioneMinore[0] = nomeChef
            competizioneMinore[1] = piatto
            competizioneMinore[2] = punteggio
            competizioneMinore[3] = giudici
    return competizioneMinore

while True:
    print("[1] Ottenere la media del punteggio in tutte le competizioni;")
    print("[2] Ottenere la media del punteggio uno chef specifico;")
    print("[3] Sapere la competizione con il numero maggiore di giudici;")
    print("[4] Sapere la competizione con il numero minore di giudici;")
    print("[0] Esci")
    scelta = int(input("Quale operazione vuoi scegliere? "))
    while (scelta>4 or scelta<0):
        scelta = int(input("Scelta inserita non valida. Riprova: "))
    if (scelta == 1):
        print("Media del punteggio di ogni competizione: ")
        print(media_punteggio_competizioni(tupla_competizioni))
    elif (scelta == 2):
        chef = str(input("Inserisci il nome di uno chef: "))
        print(f"Media del punteggio dello chef {chef}: ")
        print(media_punteggio_chef(tupla_competizioni, chef))
    elif (scelta == 3):
        print("Competizione con il numero maggiore di giudici: ")
        risultato = competizione_con_piu_giudici(tupla_competizioni)
    elif (scelta == 4):
        print("Competizione con il numero minore di giudici: ")
        print(competizione_con_meno_giudici(tupla_competizioni))
    elif (scelta == 0):
        break

    

