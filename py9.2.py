while True:
    letters = input('Geef een string van vier letters: ')
    if len(letters) == 4:
        print('Inlezen van correcte string: ', end='')
        print(letters + ' is geslaagd')
        break
    elif len(letters) != 4:
        l = len(letters)
        print(letters + ' heeft ' + str(l) +' letters.')