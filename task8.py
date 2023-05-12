with open('data.txt', 'r') as file:
    a = file.readlines()
    for i in range(1, len(a)+1):
        print(a[-i].rstrip())
