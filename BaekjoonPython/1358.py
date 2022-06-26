W, H, X, Y, P = map(int, input().split())
radius = H / 2
count = 0
for i in range(P):
    personX, personY = map(int, input().split())
    #왼쪽 부분
    if X - radius <= personX <= X and Y <= personY <= Y + H:
        if ((personX - X)**2 + (personY - Y - radius)**2)**0.5 <= radius:
            count += 1
    # 중간 부분
    elif X <= personX <= X + W and Y <= personY <= Y + H:
        count += 1
    # 오른쪽 부분
    elif X + W <= personX <= X + W + radius and Y <= personY <= Y + H:
        if ((personX - X - W)**2 + (personY - Y - radius)**2)**0.5 <= radius:
            count += 1
print(count)
