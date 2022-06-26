T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 두점 사이의 거리
    dif = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    if dif == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if dif == r1 + r2 or dif == abs(r1 - r2):
            print(1)
        elif dif < r1 + r2 and dif > abs(r1 - r2):
            print(2)
        else:
            print(0)
