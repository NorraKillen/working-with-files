file = open('nums.txt', 'r')
print(sum(list(map(int, file.read().split()))))
file.close()