import sys
input = sys.stdin.readline
N = int(input())
queue1 = []
for i in range(N):
    cmd = list(input().split())
    if cmd[0] == "push":
        queue1.append(cmd[1])
    elif cmd[0] == "pop":
        if len(queue1) == 0:
            print(-1)
        else:
            print(queue1.pop(0))
    elif cmd[0] == "size":
        print(len(queue1))
    elif cmd[0] == "empty":
        if len(queue1) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if len(queue1) == 0:
            print(-1)
        else:
            print(queue1[0])
    elif cmd[0] == "back":
        if len(queue1) == 0:
            print(-1)
        else:
            print(queue1[-1])