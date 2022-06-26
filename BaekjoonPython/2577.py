A = int(input())
B = int(input())
C = int(input())

multiplied = A * B * C
multiplied2 = A * B * C

# 자리수 확인하기
count = 0
while multiplied:
    multiplied = multiplied // 10
    count += 1

result = list(0 for i in range(10))
for i in range(10):
    calculate = multiplied2
    for j in range(count):
        if int(calculate % 10) == i:
            result[i] += 1
        calculate = calculate / 10
    print(result[i])