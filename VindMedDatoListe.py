import os, json, datetime
os.chdir('C:\\Users\\Anders Herseth\\Documents')  # Flytter nåverende arbeidsmappe til denne destinasjonen

#Denne funksjonen lager en dictionary med datoer, og hvilken vind det var den dagen.
#Denne funksjonen brukes sammen med datolisteuthenting for å finne ut hvilken vind det var på gitt dag.



def datoListe(retninghastighet):
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow = str(tomorrow)
    dictliste = {}
    dictliste[tomorrow] = retninghastighet

    fil = open('C:\\Users\\Anders Herseth\\Documents\\datoliste.txt', 'r')     #Åpner filen som ligger lagret
    lesefil = fil.read()                                                        #Leser filen som ligger lagret
    try: #Legger inn en try og except i tilfelle filen er tom, så krasjer ikke programmet
        dictionary = json.loads(lesefil)                                        #Gjør om filen til dictionary
    except json.decoder.JSONDecodeError:
        dictionary = {} #Hvis filen er tom, skal "dictionary" defineres som en tom dictionary
    dictionary.update(dictliste)

    #print('Dictionary med datoer og hvilken vind det var meldt den dagen:')
    #print(str(dictionary) + '\n')
    fil = open('C:\\Users\\Anders Herseth\\Documents\\datoliste.txt', 'w')   #Åpner filen i skrivemodus
    utskrift = json.dumps(dictionary)                                         #Gjør om filen til en string
    fil.write(utskrift)                                                       #Lagrer filen
    fil.close()
    return dictionary




#print('Skriv inn en ny retning og hastighet i m/s, f.eks slik: sv1')
#retninghastighet = input() #Retning og hastighet
#datoListe(retninghastighet)

