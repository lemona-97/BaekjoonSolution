import sys
N = int(sys.stdin.readline())
count = 1
next = lambda x: x % 10 * 10 + (x // 10 + x % 10) % 10
check = next(N)
if check == N:
    print(1)
else:
    while True:
        count += 1
        check = next(check)
        if check == N:
            break
    print(count)