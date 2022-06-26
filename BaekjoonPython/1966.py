import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    temp = list(input().split())
    index = deque(list(range(len(temp))))
    queue = deque(temp)
    index[M] = 'target'
    count = 0
    while True:
        if queue[0] == max(queue):
            count += 1
            if  index[0] == 'target':
                print(count)
                break
            else:
                queue.popleft()
                index.popleft()
        else:
            index.append(index.popleft())
            queue.append(queue.popleft())
