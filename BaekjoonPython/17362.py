A = int(input())

num = A % 8
if num == 0:
    print(2)
elif num >= 1 and num <6:
    print(num)
else:
    print(10-num)