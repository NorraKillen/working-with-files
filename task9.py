with open('lines.txt', 'r') as file:
    a = [i.rstrip() for i in file.readlines()]
    print(*list(filter(lambda x: x if len(x) == len(max(a, key=len)) else False, a)), sep='\n')