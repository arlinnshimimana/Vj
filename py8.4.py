studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]

def gemmiddeld_student(studentencijfers):
    s = 0
    for d in studentencijfers:
            ant = sum(studentencijfers[s])/len(studentencijfers[s])
            s += 1
            print(ant)

def gemiddelde_van_alle_studenten(studentencijfers):
    antw =  sum([sum(x) for x in studentencijfers])/ (len(studentencijfers)*3)
    return antw

gemmiddeld_student(studentencijfers)
print(gemiddelde_van_alle_studenten(studentencijfers))