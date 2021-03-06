
#Dette er masteren


#Import modules

import MatiasYr2                #open_YR()      update()         getForecast()
import YrTilListe               #meldtvind()
import Datolisteuthenting       #datoListeuthenting()
import VindMedDatoListe         #datoListe()
import HenteFlightlog           #sjekkeFlightlog()
import Flybare_dager
import Sjanseflybart
import time

Sjanseflybart.sjanseflybart()
sistkjørt = open('/home/pi/Flybart/lastrun', 'r')  # Åpner filen som ligger lagret#
sistkjørt = sistkjørt.read()                                                  # Leser filen som ligger lagret

tid = time.localtime()[3]                                                     # Tidspunkt NÅ

if str(time.localtime()[2]) != sistkjørt and tid > 18 and tid < 21:           # Skal kun kjøre mellom kl 18 og 21

        MatiasYr2.open_YR() #Henter værvarselet for dagen imorgen



        retninghastighet = str(MatiasYr2.getForecast(MatiasYr2.open_YR()))

        retninghastighet = retninghastighet.replace('(', '').replace(')', '').replace(",", "").replace("'", "") #Fjerner litt drit, kan flyttes til matias sitt program

        #YrTilListe.meldtvind(retninghastighet)#Lager liste med vind som har vært og teller kor mange dager det er
        print('Vind som har vært meldt: \n' + str(YrTilListe.meldtvind(retninghastighet)) + '\n')

        VindMedDatoListe.datoListe(retninghastighet)    #Lager liste med vind og dato
        print('Datoer med hvilken retning og styrke den dagen: \n' + str(VindMedDatoListe.datoListe(retninghastighet)) + '\n')

        Datolisteuthenting.datoListeuthenting()         #Henter hvilken vind det var for en uke siden

        Flybare_dager.flydager()
        print('Dager det var flybart med vind: \n' + str(Flybare_dager.flydager()) + '\n')

        sistkjørt = open('/home/pi/Flybart/lastrun', 'w')  # Åpner filen som ligger lagret#
        sistkjørt.write(str(time.localtime()[2]))                                              # Leser filen som ligger lagret
        sistkjørt.close()

