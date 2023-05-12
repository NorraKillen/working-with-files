with open('numbers.txt', 'r') as file:
    a = [list(map(int, i.split())) for i in file.readlines()]
    print(*list(map(sum, a)), sep='\n')