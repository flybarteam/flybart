# Import modules
import urllib.request
import xml.etree.ElementTree as ET
import time


def open_YR():
    Ulriken_XML = ET.parse(urllib.request.urlopen('https://www.yr.no/sted/Norge/Hordaland/Bergen/Ulriken/varsel.xml'))
    root = Ulriken_XML.getroot()
    return root


def update(root):
    # Get next / Last update.
    open_YR()
    for LU in root.iter('lastupdate'):
        Lastupdate = LU.text
    for NU in root.iter('nextupdate'):
        Nextupdate = NU.text
        Lastupdate = LU.text

    return Nextupdate, Lastupdate


def getForecast(root):
    open_YR()
    windDirection = []
    windSpeed = []
    period = []
    rain = []
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

    # Getting rain forecast from YR
    for R in root.iter('precipitation'):
        rain.append(str(round(float(R.get('value')))))

    # Returning first forecast for period 12:00 to 18:00
    # If local time is 12:00 or earlier, it will show the forecast for the current day.
    # if local time is past 12:00, it will show the forecast for the next day.
    tmp = 0
    if time.localtime()[3] < 12:
        while period[tmp] != '2':
            tmp += 1
    else:
        tmp = 3
        while period[tmp] != '2':
            tmp += 1
        # Adding '-R' to the end of the wind direction if it's rainy
    if rain[tmp] != '0':
        windDirection[tmp] = windDirection[tmp] + '-R'
    return windDirection[tmp], windSpeed[tmp]

root = open_YR()
testing = getForecast(root)
update(root)
Update_time = update(root)
Nextupdate = Update_time[0]
Lastupdate = Update_time[1]
Lastupdate_H = Lastupdate[11:13]
Lastupdate_M = Lastupdate[14:16]
Nextupdate_H = Nextupdate[11:13]
Nextupdate_M = Nextupdate[14:16]

while time.localtime()[3] < int(Nextupdate_H)-2:
    if __name__ == "__main__":
        print('Waiting for next update')
        print('Last update was', Lastupdate_H + ':' + Lastupdate_M)
        print('Next update is scheduled to', Nextupdate_H + ':' + Nextupdate_M)
        print('.................................')
    time.sleep(5)

while Lastupdate == update(root)[1]:
    update(root)
    Nextupdate = update(root)[0]
    time.sleep(10)
    if __name__ == "__main__":
        print('Slept for 5 minutes')
        print('Still no new update...')
        print('Will try again in 5 minutes')
        print('...........................')

if __name__ == "__main__":
    print(Nextupdate)
    print(Nextupdate_H)
    print(Nextupdate_M)
    print(Lastupdate)
    print(time.localtime()[3])
    print(getForecast(root))