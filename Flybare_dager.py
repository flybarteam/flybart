import HenteFlightlog
import Datolisteuthenting
import VindMedDatoListe
import YrTilListe
import MatiasYr2
def flydager():
    flybaredager = {}                               #Lager ny dictionary med flybare dager
    retninghastighet = str(MatiasYr2.getForecast(MatiasYr2.open_YR()))  # Henter værvarselet for dagen imorgen
    retninghastighet = retninghastighet.replace('(', '').replace(')', '').replace(",", "").replace("'", "")
    #print(HenteFlightlog.sjekkeFlightlog())
    datoliste = VindMedDatoListe.datoListe(retninghastighet) #må legge noe inn her hvis du vil kjøre kun denne funksjonen
    dato = HenteFlightlog.sjekkeFlightlog()


    #print(datoliste[dato])

    if dato in datoliste.keys():
        if dato not in flybaredager.keys():     #Hvis denne datoen finnes ikke finnes fra før, lages det ny
            flybaredager.setdefault(datoliste[dato], 1)


        if dato in flybaredager.keys():     #Hvis denne datoent finnes fra før plusses det på 1.
            flybaredager[dato] += 1

    return flybaredager
