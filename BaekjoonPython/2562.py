number = []
for _ in range(9):
    number.append(int(input()))

max = 0
maxidx = 0
for i in range(0, 9):
    if number[i] > max:
        max = number[i]
        maxidx = i+1
print(max)
print(maxidx)