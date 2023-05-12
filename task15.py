def read_csv():
    with open('data.csv', 'r') as file:
        keys = file.readline().strip().split(',')
        k = [i.split(',') for i in file.read().split('\n')]
        lst = []
        for value in k:
            lst.append(dict(zip(keys, value)))
        del lst[-1]
        return lst