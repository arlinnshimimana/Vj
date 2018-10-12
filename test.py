Bestand = "hardlopers.txt"
infile = open('hardlopers', 'w')


def strftime(naam):
    import datetime
    vandaag = datetime.datetime.today()
    tijd = datetime.datetime.now()
    s = vandaag.strftime("%a %d %b %Y") + ', ' + tijd.strftime("%H:%M:%S") + ', ' + naam + '\n'

    infile.write(s)
    infile.close

    return


print('\nOm dit programma af te sluiten druk je op enter.')

while True:

    kandidaat = str(input("Geef naam van de kandidaat op: "))
    if kandidaat != '':
       strftime(kandidaat)
    else:
        print('Tot ziens')
        break