numbers = list(range(1, 21))

for i in range(10):
    a, b = map(int, input().split())
    front = numbers[:a-1]
    mid = numbers[a-1:b][::-1]
    back = numbers[b:]
    numbers = front+mid+back

for i in range(20):
    print(numbers[i])