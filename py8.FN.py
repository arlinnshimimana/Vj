aantal_kluizen = 12
def menu():
    menu = ['1: ik wil weten hoeveel kluizen vrij zijn','2: ik wil een nieuwe kluis','3: ik wil even iets terug halen uit mijn kluis','4: ik geef mijn kluis terug','5: Sluit']

    for i in menu:
        print(i)

def aantal_kluizen_vrij():
    file = open('kluizen.txt', 'r')
    lines = []
    lines.extend(file.readlines())

    aantal_regels = len(lines)
    print(aantal_kluizen - aantal_regels)
    file.close()

def nieuwe_kluis():
    file = open('kluizen.txt', 'r+')
    regellijst = file.readlines()
    list = [1,2,3,4,5,6,7,8,9,10,11,12]

    for regel in regellijst:
        kluis_combinatie = regel.split(';')
        kluis_nummer = kluis_combinatie[0]
        list.remove(int(kluis_nummer))

    if len(list) > 0 :
        print('Dit zijn de kluizen die nog vrij zijn ' + str(list))
        nieuw_nummer = list[0]
        print('Uw kluisnummer is: ' + str(nieuw_nummer))
        code = input('Geef uw code op: ')
        file.writelines('\n' + str(nieuw_nummer) + ';' + code)

    else:
        print('Sorry, alle kluizen zijn bezet')
    file.close()



def open_kluis():
    file = open('kluizen.txt', 'r')
    t = file.readlines()
    kluis_nummer = str(input('kluisnummer: '))
    wachtwoord = str(input('wachtwoord: '))
    combinatie = False

    for i in t:
        e = i.split(';')
        z = e[0]
        h = e[1]

        if kluis_nummer == z and wachtwoord in h:
            print('Kluis geopend ')
            combinatie = True
            break

    if combinatie == False:

        print('De combinatie kluisnummer en wachtwoord is incorrect')

def kluis_terug():
    file = open('kluizen.txt', 'r+')
    kluis_info = file.readlines()
    k = input('wat is uw kluisnummer: ')
    w = input('Wat is uw code: ')
    file.seek(0)

    for i in kluis_info:

        e = i.split(';')

        if str(w) not in i and k != e[0]:

            file.write(i)

    file.truncate()

    file.close()

    print('uw kluis is teruggegeven')

while True:
    menu()
    print()
    kies_menu = input('Kies een menu: ')
    if kies_menu == '1':
        print()
        print('Het aantal vrije kluizen is: ', end='')
        aantal_kluizen_vrij()
        print()


    elif kies_menu == '2':
        nieuwe_kluis()

    elif kies_menu == '3':
         open_kluis()
         print()
    elif kies_menu == '4':
        kluis_terug()
    elif kies_menu == '5':
        break
    else:
        print('Menu bestaat niet!')
    print()
    print('------------------------------')

