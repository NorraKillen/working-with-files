import random
with open('random.txt', 'w') as file:
    for i in range(25):
        file.write(f'{random.randint(111, 777)}\n')