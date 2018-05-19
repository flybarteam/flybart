import HenteFlightlog
import VindMedDatoListe
import MatiasYr2
import json

#Denne funksjonen lager en dictionary med kor mange ganger det har vært flybart med forskjellig vind. Den gjør det ved å sjekke


def flydager():


    fil = open('C:\\Users\\Anders Herseth\\Documents\\flybaredager.txt', 'r')   # Åpner filen som ligger lagret
    lesefil = fil.read()                                                        # Leser filen som ligger lagret
    try:                                                                        # Legger inn en try og except i tilfelle filen er tom, så krasjer ikke programmet
        dictionary = json.loads(lesefil)                                        # Gjør om filen til dictionary
    except json.decoder.JSONDecodeError:
        dictionary = {}                                                         # Hvis filen er tom, skal "dictionary" defineres som en tom dictionary

    flybaredager = dictionary



    retninghastighet = str(MatiasYr2.getForecast(MatiasYr2.open_YR()))                                      # Henter værvarselet for dagen imorgen
    retninghastighet = retninghastighet.replace('(', '').replace(')', '').replace(",", "").replace("'", "") # Tar vekk litt unødvendige karakterer


    datoliste = VindMedDatoListe.datoListe(retninghastighet)    # Henter listen med datoer og vind
    dato = HenteFlightlog.sjekkeFlightlog()                     # Henter datoen som skal sjekkes om var flybar



    if dato in datoliste.keys():                                # Hvis det var flybart på gitt dag:
        if dato not in flybaredager.keys():                     #Hvis denne datoen finnes ikke finnes fra før, lages det ny
            flybaredager.setdefault(datoliste[dato], 1)


        if dato in flybaredager.keys():                         #Hvis denne datoent finnes fra før plusses det på 1.
            flybaredager[dato] += 1

    fil2 = open('C:\\Users\\Anders Herseth\\Documents\\flybaredager.txt', 'w')  # Åpner filen i skrivemodus
    utskrift = json.dumps(flybaredager)                                         # Gjør om filen til en string
    fil2.write(utskrift)                                                        # Lagrer filen
    fil2.close()                                                                # Lukker filen




    return flybaredager
