file = open('prices.txt', 'r')
a = []
for i in file.readlines():
    line = i.split()
    a.append(int(line[1])*int(line[2]))
print(sum(a))
file.close()