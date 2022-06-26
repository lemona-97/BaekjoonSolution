import sys
K, L = map(int, sys.stdin.readline().split())
waiting = {}
for i in range(L):
    stuNumber = sys.stdin.readline().rstrip()
    waiting[stuNumber] = i

waiting = sorted(waiting.items(), key=(lambda  x: x[1]))

count = 0
for i in waiting:
    if count == K:
        break
    print(i[0])
    count += 1