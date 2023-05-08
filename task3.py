import random
file = open('lines.txt', 'r')
print(random.choice(file.readlines()))
file.close()