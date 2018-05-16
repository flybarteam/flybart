
#Dette er masteren


#Import modules
import urllib.request
import xml.etree.ElementTree as ET
import os, json
import MatiasYr2
import YrTilListe
import Datolisteuthenting
import VindMedDatoListe

MatiasYr2.open_YR()



retninghastighet = str(MatiasYr2.getForecast(MatiasYr2.open_YR()))

retninghastighet = retninghastighet.replace('(', '').replace(')', '').replace(",", "").replace("'", "")

YrTilListe.meldtvind(retninghastighet)
VindMedDatoListe.datoListe(retninghastighet)

Datolisteuthenting.datoListeuthenting()


