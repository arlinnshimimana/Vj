fr = open('kaartnummers.txt', 'r')

text = fr.readlines()
for i in text:
    a = i.split(',')
    print(a[1] + 'heeft kaartnummer:' + a[0])
fr.close()