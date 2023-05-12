def minutes(x):
    res = [int(i) for i in x.split(':')]
    return res[0]*60+res[1]
with open('logfile.txt', 'r') as inp, open('output.txt', 'w') as file:
    dl = len(inp.readlines())
    inp.seek(0)
    for j in range(dl):
        a, b, c = inp.readline().split(',')
        suma = abs(minutes(b)-minutes(c))
        if suma >= 60:
            file.write(a+'\n')