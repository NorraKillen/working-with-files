with open('population.txt', 'r') as file:
    names = [i.strip().split() for i in file.readlines()]
    a = filter(lambda x: x if x[0][0] == 'G' and int(x[-1]) > 500000 else False,  names)
    for i in a:
        print(i[0])