import os, json
os.chdir('C:\\Users\\Anders Herseth\\Documents')  # Flytter nåverende arbeidsmappe til denne destinasjonen



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

    #print('Vind som har vært meldt: ' + str(vind) +'\n')
    fil = open('C:\\Users\\Anders Herseth\\Documents\\værmeldinger.txt', 'w')   #Åpner filen i skrivemodus
    utskrift = json.dumps(vind)                                               #Gjør om filen til en string
    fil.write(utskrift)                                                       #Lagrer filen
    fil.close()            #Lukker filen
    return vind




#print('Skriv inn en ny retning og hastighet i m/s, f.eks slik: sv1')
#retninghastighet = input() #Retning og hastighet
#meldtvind(retninghastighet)

