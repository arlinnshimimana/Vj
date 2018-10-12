def gemiddelde():
    zin = input('wat is jouw zin:')
    Woorden_list = zin.split(' ')
    hoeveel_woorden = len(Woorden_list)
    sum_woorden = 0
    for i in Woorden_list:
        sum_woorden += len(i)
        ant = sum_woorden/hoeveel_woorden
    return ant


print(gemiddelde())