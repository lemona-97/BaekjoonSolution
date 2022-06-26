import sys
input = sys.stdin.readline
N = int(input())
result = []
info = int(input())

while info != -1:
    if info == 0:
        result.pop(0)
    else:
        if len(result) > N:
            info = int(input())
            continue
        else:
            result.append(info)
    info = int(input())
if len(result) == 0:
    print("empty")
else:
    for i in range(len(result)):
        print(result[i], end=" ")