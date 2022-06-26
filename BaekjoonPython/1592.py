N, M, L = map(int, input().split())

people = [0]*N
count = 0
i = 0
while people[i] < M - 1:
    people[i] += 1
    count += 1
    if people[i] % 2 == 1:
        i = (i + L) % N
    else:
        i = (i - L) % N
print(count)