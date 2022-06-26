
N = int(input())
stack = []
result = []
for i in range(N):
    operation = list(input().split())
    if operation[0] == 'push':
        stack.append(operation[1])
    elif operation[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            result.append(stack.pop())
    elif operation[0] == 'size':
        result.append(len(stack))
    elif operation[0] == 'empty':
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
    elif operation[0] == 'top':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[-1])
for i in range(len(result)):
    print(result[i])