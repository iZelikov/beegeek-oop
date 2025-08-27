n = 3
m = 5
matrix = [[f'{i} {j}' for j in range(n)] for i in range(m)]
trans = list(map(list, zip(*matrix)))
print(*matrix, sep = "\n")
print(*trans, sep = '\n')