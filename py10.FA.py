def inlezen_beginstation(stations):
    while True:
        st = input('Wat is uw begin station?: ')
        if st in stations:
            break
    return st
def inlezen_eindstation(stations, beginstation):
    while True:
        et = input('Wat is je eindstation?: ')
        if et not in stations:
            print('Deze trein gaat niet naar ' + str(et))
        elif stations.index(et) < stations.index(beginstation):
            print('Deze halte is al geweest')
        else:
            break
        print()
    return et
def omroepen_reis(stations, beginstation, eindstation):
    a = stations.index(beginstation)
    b = stations.index(eindstation)
    c = int(b-a)

    print()
    print('Het beginstation ' + beginstation + 'Is het ' + str((stations.index(beginstation))+1)+ 'e in het traject')
    print('Het eindstation ' + eindstation + ' is het ' + str((stations.index(eindstation))+1)+ 'e in het traject')
    print('De afstand bedraagt ' + str(b-a) + ' station(s)')
    print('De prijs van de kaartje is '+str(c * 5) + ' euro')
    print('Jij stapt in de trein in: ' + beginstation)
    for i in stations:
        if a < stations.index(i) < b:
            print('-' + i)
    print('Jij stapt uit in: '+ eindstation)
    print('Fijne rijs!')



stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel","Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven","Weert", "Roermond","Sittard", "Maastricht"]

while True:
    beginstation = inlezen_beginstation(stations)
    eindstation = inlezen_eindstation(stations, str(beginstation))
    omroepen_reis(stations, beginstation, eindstation)