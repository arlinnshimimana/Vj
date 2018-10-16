def code(invoerstring):
    b = []
    for l in invoerstring:
        a = ord(l) + 3
        b.append(a)
    c = [chr(n) for n in b]
    d = ''
    for s in c:
        d += s
    print(d)
code()
