with open('input.txt', 'r') as file:
    with open('output.txt', 'w') as file1:
        a = file.readlines()
        for i in range(1, len(a)+1):
            file1.write(f'{i}) {a[i-1]}')