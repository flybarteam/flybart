import json
import datetime as DT

#Denne funksjonen henter ut hvilken vind det var ved gitt dato. Brukes sammen med Vind med dato liste



def datoListeuthenting():
    today = DT.date.today()
    week_ago = today - DT.timedelta(days=7)
    week_ago = str(week_ago)
    fil = open('C:\\Users\\Anders Herseth\\Documents\\datoliste.txt', 'r')  # Åpner filen som ligger lagret
    lesefil = fil.read()  # Leser filen som ligger lagret
    try:  # Legger inn en try og except i tilfelle filen er tom, så krasjer ikke programmet
        dictionary = json.loads(lesefil)  # Gjør om filen til dictionary
    except json.decoder.JSONDecodeError:
        dictionary = {}  # Hvis filen er tom, skal "dictionary" defineres som en tom dictionary

    vind = dictionary  # Kanskje denne ikkje trengs?
    if week_ago in vind.keys():
        return vind[week_ago]

datoListeuthenting()
print(datoListeuthenting())