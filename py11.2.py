def s():
    import datetime
    import csv

    bestand = 'inloggers.csv'
    with open(bestand, 'w', newline='') as f:
         e = csv.writer(f)
        e.writerow

    # gebruik hier een herhalingslus:
    while True:
        n = ['einde']
        naam = input("Wat is je achternaam? ")
        if len(naam) > 0:
            voorl = input("Wat zijn je voorletters? ")
            gbdatum = input("Wat is je geboortedatum? ")
            email = input("Wat is je e-mail adres? ")
            print()
        elif len(naam) == 0:
            print()
            break
        file.write(s())
s()