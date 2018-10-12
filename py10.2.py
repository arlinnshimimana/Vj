def monepoly():
    import random
    while True:
        a = random.randrange(1, 6)
        b = random.randrange(1, 6)
        if a != b:
            print( str(a) + ' + ' + str(b) + ' = ' + str(a + b))
            break
        elif a == 2 and b == 2:
            print(str(a) + ' + ' + str(b) + ' = ' + str(a+b) + ' direct naar de gevangenis')
            break
        elif a == b:
            print(str(a) + ' + ' + str(b) + ' = ' + str(a + b) + '(dubble)')
monepoly()