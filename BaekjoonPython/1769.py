count = 0


def change(num, cnt):
    if len(num) > 1:
        cnt += 1
        n = 0
        for i in num:
            n += int(i)
        change(str(n), cnt)
    else:
        print(cnt)
        if int(num) % 3 == 0:
            print("YES")
        else:
            print("NO")


N = input()

change(N, count)
