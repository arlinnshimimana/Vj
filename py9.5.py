naam_list = []
def namen():
    while True:
        coin = {}
        naam = input('volgende naam: ')
        if naam != '':
            naam_list.append(naam)
        elif naam == '':
            print(naam_list)
            break
    for n in naam_list:
        if n in coin:
            coin[n] += 1
        else:
            coin[n] = 1
    for n in coin:
        if coin[n] > 1:
            print('Er zijn {} studenten met de naam {}'.format(coin[n], n))
        else:
            print('Er is {} student met de naam {}'.format(coin[n], n))
namen()
