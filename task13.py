import random
def nasur():
    with open('first_names.txt', 'r') as name:
        names = random.choice(name.read().split())
    with open('last_names.txt', 'r') as surname:
        sname = random.choice(surname.read().split())
    return names, sname
print(*nasur())
print(*nasur())
print(*nasur())