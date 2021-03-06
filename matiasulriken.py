#Import modules
import urllib.request
import xml.etree.ElementTree as ET

Ulriken_XML = ET.parse(urllib.request.urlopen('https://www.yr.no/sted/Norge/Hordaland/Bergen/Ulriken/varsel.xml'))
root = Ulriken_XML.getroot()
windDirection = []
windSpeed = []
period = []
tmp = 0

# Getting windspeed from YR
for WS in root.iter('windSpeed'):
    windSpeed.append(WS.get('mps'))

# Getting wind direction from YR
for WD in root.iter('windDirection'):
    windDirection.append(WD.get('code'))

for T in root.iter('time'):
    if T.get('period') is not None:
        period.append(T.get('period'))

# Printing the result
for a in windDirection:
    try:
        while period[tmp] == '0' or period[tmp] == '3':
            tmp = tmp + 1
    except IndexError:
        None

    try:
        print(windSpeed[tmp], windDirection[tmp], period[tmp])
    except IndexError:
        None
    tmp = tmp + 1