file = open('numbers.txt', 'r')
print(sum(list(map(int, file.readlines()))))
file.close()