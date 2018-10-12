list = eval(input("Geef lijst met minimaal 10 strings: "))

list2 = []
for stings in list:
    if len(stings) == 4:
        list2.append(stings)

print('De nieuw gemmakt lijst met vier-letter strings is:')
print(list2)