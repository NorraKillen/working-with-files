with open('goats.txt', 'r') as fileinput, open('answer.txt', 'w') as file:
    a = []
    for i in fileinput:
        if i == 'GOATS\n':
            break
    for i in fileinput:
        if i == 'Black goat':
            i = 'Black goat\n'
        a.append(i)

    b = {}
    for i in a:
        if b.get(i, None):
            b[i] += 1
        else:
            b[i] = 1
    for i in b:
        if b[i]/len(a) > 0.07:
            print(i.strip())