def standaardprijs(afstandkm):
    if 0 < afstandkm < 50:
        treinrit = 0.80*afstandkm
    elif afstandkm >= 50:
        treinrit = 0.60*afstandkm + 15
    else:
        treinrit = 0
    return  treinrit


print(standaardprijs(0))

def ritprijs(leeftijd, weekendrit, afstandkm):
    if 12 > leeftijd or leeftijd >= 65:

        tarief = standaardprijs(afstandkm)*0.70

    elif (12 > leeftijd or leeftijd >= 65) and weekendrit == True:

       tarief = standaardprijs(afstandkm)*0.65

    elif 12 <= leeftijd < 65 and weekendrit == True:

        tarief = standaardprijs(afstandkm)*0.60
    else:

        tarief = standaardprijs(afstandkm)

    return tarief

print(ritprijs(65,True,40))
