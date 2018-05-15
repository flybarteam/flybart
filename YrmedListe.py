#Import modules
import urllib.request
import xml.etree.ElementTree as ET
import os, json
os.chdir('C:\\Users\\Anders Herseth\\Documents')  # Flytter nåverende arbeidsmappe til denne destinasjonen
Ulriken_XML = ET.parse(urllib.request.urlopen('https://www.yr.no/sted/Norge/Hordaland/Bergen/Ulriken/varsel.xml'))
root = Ulriken_XML.getroot()

def meldtvind(retninghastighet):
    global vind                                                                 #Gjør vind variabel om til global
    fil = open('C:\\Users\\Anders Herseth\\Documents\\værmeldinger.txt', 'r')     #Åpner filen som ligger lagret
    lesefil = fil.read()                                                        #Leser filen som ligger lagret
    try: #Legger inn en try og except i tilfelle filen er tom, så krasjer ikke programmet
        dictionary = json.loads(lesefil)                                        #Gjør om filen til dictionary
    except json.decoder.JSONDecodeError:
        dictionary = {} #Hvis filen er tom, skal "dictionary" defineres som en tom dictionary


    vind = dictionary                           #Kanskje denne ikkje trengs?

    if retninghastighet not in vind.keys():     #Hvis denne retningen og hastighet ikke finnes fra før, lages det ny
        vind.setdefault(retninghastighet, 0)

    if retninghastighet in vind.keys():         #Hvis denne retningen og hastighet finnes fra før, plusses det på 1
        vind[retninghastighet] += 1

    print(vind)
    fil = open('C:\\Users\\Anders Herseth\\Documents\\værmeldinger.txt', 'w')   #Åpner filen i skrivemodus
    utskrift = json.dumps(vind)                                               #Gjør om filen til en string
    fil.write(utskrift)                                                       #Lagrer filen
    fil.close()                                                               #Lukker filen
    return vind

def update():
    # Get next / Last update.
    for LU in root.iter('lastupdate'):
     Lastupdate = LU.text
    for NU in root.iter('nextupdate'):
        Nextupdate = NU.text
        Lastupdate = LU.text

    return Nextupdate, Lastupdate

def getForecast():
    windDirection = []
    windSpeed = []
    period = []
    tmp = 0
    # Getting windspeed from YR
    for WS in root.iter('windSpeed'):
        windSpeed.append(str(round(float(WS.get('mps')))))

    # Getting wind direction from YR
    for WD in root.iter('windDirection'):
        windDirection.append(WD.get('code'))

    for T in root.iter('time'):
        if T.get('period') is not None:
            period.append(T.get('period'))

    # Returning first forecast for period 12:00 to 18:00
    tmp = 0
    while period[tmp] != '2':
        tmp = tmp + 1
    return windDirection[tmp], windSpeed[tmp]

#print(update())
#print(getForecast())

retninghastighet = str(getForecast())
retninghastighet = retninghastighet.replace('(', '').replace(')', '').replace(",", "").replace("'", "") # Dette for å fjerne litt characters
meldtvind(retninghastighet)
