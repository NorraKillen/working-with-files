import re
with open('nums.txt', 'r') as file:
    my_list = [re.findall(r'\d+', line) for line in file.readlines()]
    print(sum(list(map(lambda x: sum(list(map(int, x))), my_list))))