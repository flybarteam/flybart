import MatiasYr2
import json

#Dette programmet lager en fil "vindinfo" der det står bakgrunnen for at meldingen er slik den er.
def vindinfoen():

    MatiasYr2.open_YR() #Henter værvarselet for dagen imorgen

    retninghastighet = str(MatiasYr2.getForecast(MatiasYr2.open_YR()))
    retninghastighet = retninghastighet.replace('(', '').replace(')', '').replace(",", "").replace("'", "") #Fjerner litt drit, kan flyttes til matias sitt program

    fil = open('C:\\Users\\Anders Herseth\\Documents\\flybaredager.txt', 'r')  # Åpner filen som ligger lagret
    lesefil = fil.read()  # Leser filen som ligger lagret
    try:  # Legger inn en try og except i tilfelle filen er tom, så krasjer ikke programmet
        dictionary = json.loads(lesefil)  # Gjør om filen til dictionary
    except json.decoder.JSONDecodeError:
        dictionary = {}  # Hvis filen er tom, skal "dictionary" defineres som en tom dictionary

    flybaredager = dictionary

    fil2 = open('C:\\Users\\Anders Herseth\\Documents\\værmeldinger.txt', 'r')     #Åpner filen som ligger lagret
    lesefil2 = fil2.read()                                                        #Leser filen som ligger lagret
    try: #Legger inn en try og except i tilfelle filen er tom, så krasjer ikke programmet
        dictionary2 = json.loads(lesefil2)                                        #Gjør om filen til dictionary
    except json.decoder.JSONDecodeError:
        dictionary2 = {} #Hvis filen er tom, skal "dictionary" defineres som en tom dictionary

    værmeldinger = dictionary2

    vindinfo = open('C:\\Users\\Anders Herseth\\Documents\\vindinfo.txt', 'w')  # Åpner filen som ligger lagret
    try:
        vindinfo.write('Bakgrunnen for dette er at:\n' + str(retninghastighet) + ' har vært meldt ' +
        (str(værmeldinger[retninghastighet]) + ' gang(er)\n' + str(retninghastighet) +
        ' har vært flybar ' + (str(flybaredager[retninghastighet]) + ' gang(er)')))                                        # Skriver til filen
    except KeyError:
        vindinfo.write('Flybart har dessverre ikke nok data til å gi deg et svar for imorgen')
    vindinfo.close()

    try:
        print('Bakgrunnen for dette er at:\n' + str(retninghastighet) + ' har vært meldt ' +
            (str(værmeldinger[retninghastighet]) + ' gang(er)\n' + str(retninghastighet) +
            ' har vært flybar ' + (str(flybaredager[retninghastighet]) + ' gang(er)')))
    except KeyError:
        print('Flybart har dessverre ikke nok data til å gi deg et svar for imorgen')



    print(retninghastighet)
	print("Test")