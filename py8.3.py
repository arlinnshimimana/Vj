invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
vin = invoer.split('-')
vin.sort()
n = [int (i) for i in vin]
g = sum(n)/len(vin)

print('Gesorteerde list van ints:' + str(vin))
print('grootste getal:'+' '+max(vin) + ' ' + 'en kleinste getal:' + ' ' + min(vin))
print('Aantal getallen:', end=' ')
print(len(vin))
print('som van gettalen:', end=' ')
print(sum(n))
print('gemiddelde :', end=' ')
print(g)
