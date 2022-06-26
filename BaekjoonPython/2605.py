
studentNum = int(input())
number = list(map(int, input().split()))
sort = []

for i in range(0, studentNum):
    sort.insert(number[i], i+1)

sort = sort[::-1]

print(*sort)
