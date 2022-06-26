import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

queue1 = deque(list(range(1, N+1)))
while len(queue1) > 1:
    queue1.popleft()
    queue1.append(queue1.popleft())
print(queue1[0])
