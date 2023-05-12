with open('class_scores.txt', 'r') as file:
    with open('new_scores.txt', 'w') as file1:
        a = [i.split() for i in file.readlines()]
        for i in a:
            if int(i[1]) >= 96:
                i[1] = str(100)
            else:
                i[1] = str(int(i[1]) + 5)
        for i in a:
            file1.writelines(f'{i[0]} {i[1]}\n')