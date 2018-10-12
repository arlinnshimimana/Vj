def ticker(filename):
    file = open(filename, 'r')
    d = {}
    for line in file:
        e = line.split(':')
        a = e[0]
        b = e[1]
        c = len(b)-1
        d[a] = b[0:c]
    while True:
        try:
           naam = input('enter the companys name: ')
           print('ticker symbool: ' + d[naam])
           symbool = input('enter the ticker symbol: ')
           for key, value in d.items():
               if value == symbool:
                  print('company name: ' + key)
        except:
               print('d')
        print()


while True:
    ticker('tickers.txt')
    print('druk enter als je wilt stoppen')
    if input() == '':
        break
    else:
        continue