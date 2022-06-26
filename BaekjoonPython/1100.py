chess = []

for i in range(8):
    chess.append(list(map(str, input())))
count = 0
for i in range(8):
    if i == 0 or i == 2 or i == 4 or i == 6:
        for j in range(8):
            if j % 2 == 0:
                if chess[i][j] == 'F':
                    count += 1
    if i == 1 or i == 3 or i == 5 or i == 7:
        for k in range(8):
            if k % 2 == 1:
                if chess[i][k] == 'F':
                    count += 1

print(count)