import MatiasYr2
import json
import datetime as DT

#Dette programmet tar og henter kor mange ganger det har vært meldt vinden som er meldt imorgen og hvor mange ganger
#det har vært flybart med denne vinden og regner ut i % kor stor sjanse det er for at det er flybart.

def sjanseflybart():
    retninghastighet = str(MatiasYr2.getForecast(MatiasYr2.open_YR()))

    retninghastighet = retninghastighet.replace('(', '').replace(')', '').replace(",", "").replace("'", "")

    værmeldinger = open('C:\\Users\\Anders Herseth\\Documents\\værmeldinger.txt', 'r')  # Åpner filen som ligger lagret
    lesevær = værmeldinger.read()                                                       # Leser filen som ligger lagret

    try:                                # Legger inn en try og except i tilfelle filen er tom, så krasjer ikke programmet
        listevær = json.loads(lesevær)  # Gjør om filen til dictionary
    except json.decoder.JSONDecodeError:
        dictionary = {}                 # Hvis filen er tom, skal "dictionary" defineres som en tom dictionary


    flybaredager = open('C:\\Users\\Anders Herseth\\Documents\\flybaredager.txt', 'r')  # Åpner filen som ligger lagret
    lesefly = flybaredager.read()                                                       # Leser filen som ligger lagret

    try:                                # Legger inn en try og except i tilfelle filen er tom, så krasjer ikke programmet
        listefly = json.loads(lesefly)  # Gjør om filen til dictionary
    except json.decoder.JSONDecodeError:
        dictionary = {}                 # Hvis filen er tom, skal "dictionary" defineres som en tom dictionary

    today = DT.date.today()
    tomorrow = today + DT.timedelta(days=1)

    try:
        sjanseflybart = listefly[retninghastighet] / listevær[retninghastighet] * 100 #Deler flybaredager på meldt vind, ganger 100
    except KeyError:
        None

    try:
        print('Sjanse for at det er flybart imorgen ' + str(tomorrow) + ': ' + str(round(float(sjanseflybart))) + '%')
    except UnboundLocalError:
        print('Sjanse for at det er flybart imorgen : 0 %')


    try:
        flysjanse = open('C:\\Users\\Anders Herseth\\Documents\\flysjanse.txt', 'w')  # Åpner filen som ligger lagret
        flysjanse.write(str(sjanseflybart))                                           # Skriver til filen
        flysjanse.close()                                                             # Lukker filen
    except UnboundLocalError:
        flysjanse = open('C:\\Users\\Anders Herseth\\Documents\\flysjanse.txt', 'w')  # Åpner filen som ligger lagret
        flysjanse.write('0%')  # Skriver til filen
        flysjanse.close()
