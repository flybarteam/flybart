#Import modules
import requests, bs4
import datetime as DT


def sjekkeFlightlog():
    res = requests.get('https://flightlog.org/fl.html?l=1&country_id=160&start_id=253&a=42') #Ulriken
    datoSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    datoSoup = str(datoSoup)

    today = DT.date.today()
    week_ago = today - DT.timedelta(days=7)
    week_ago = str(week_ago)


    if week_ago in datoSoup:
        #print('Ja, det ble flydd: ' + week_ago)
        return week_ago
    else:
        print('Nei, det ble ikkje flydd ' + week_ago)

