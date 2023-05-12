with open('file.txt', 'r') as file:
    a = len(file.read().split())
    file.seek(0)
    b = len(file.readlines())
    file.seek(0)
    c = sum([len([i for i in j if i.isalpha()]) for j in file.read().split()])
    print('Input file contains:', f'{c} letters', f'{a} words', f'{b} lines', sep='\n')