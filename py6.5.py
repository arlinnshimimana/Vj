
def kwadraten_som(grondgetallen):
    x = 0
    for positief in grondgetallen:
        if positief > 0:
          x += positief**2
    return x


print(kwadraten_som([3, 6, 1, -6, 4, -86]))
