file = open('kaartnummers.txt', 'r')

text = file.read()

text1 = text.split('\n')

maxV = max(text1)


print('deze file telt ' + str(len(text1))+ ' regels.')

maxV_s = maxV.split(',')

print('De groostse kaartnummer is: ' + maxV_s[0] + ' en dat staat op regel ' + (str(text1.index(maxV) + 1 )))

file.close()