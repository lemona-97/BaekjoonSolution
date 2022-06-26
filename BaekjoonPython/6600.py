
while True:
    try:
        x1, y1, x2, y2, x3, y3 = map(float, input().split())
        a = ((x1-x2)**2 + (y1-y2)**2)**0.5
        b = ((x2-x3)**2 + (y2-y3)**2)**0.5
        c = ((x3-x1)**2 + (y3-y1)**2)**0.5
        s = 1 / 2 * ((x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x2*y1 + x3*y2))
        r = a*b*c/4/s
        # 반지름 r
        print(f"{round(abs(2 * r * 3.141592653589793), 2)}")

    except:
        break
