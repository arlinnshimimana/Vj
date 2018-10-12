def convert(temperatuurcelsius):
    fahrenheit = temperatuurcelsius * 1.8 + 32
    return fahrenheit


print(convert(25))


def table(n):
    for i in range(0, 80, 10):
        celsius = n + i
        print(celsius, end=' ')
        print(convert(celsius))

print(table(-30))