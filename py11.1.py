try:
    n = int(input('Met hoeveel personen reist u ?: '))
    if n < 0:
        print('Alleen positieve nummers')
    else:
        print(4356/n)
except ZeroDivisionError:
    print('Je kan niet door 0 delen')
except ValueError:
    print('Geef aan met cijfers')
except:
    print('Other errors sdkjfskdjf')
