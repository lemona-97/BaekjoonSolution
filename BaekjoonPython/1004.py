T = int(input())
for _ in range(T):
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    starList = []
    for i in range(n):
        star = list(map(int, input().split()))
        starList.append(star)
    for i in range(n):
        if ((starList[i][0] - x1)**2 + (starList[i][1] - y1)**2)**0.5 > starList[i][2]:
            if ((starList[i][0] - x2)**2 + (starList[i][1] - y2)**2)**0.5 < starList[i][2]:
                count += 1
        if ((starList[i][0] - x2)**2 + (starList[i][1] - y2)**2)**0.5 > starList[i][2]:
            if ((starList[i][0] - x1)**2 + (starList[i][1] - y1)**2)**0.5 < starList[i][2]:
                count += 1
    print(count)
#행성을 하나만 포함하는경우
# 카운트 +1
#행성을 둘다 포함하는 경우
# 카운트 x