import datetime
def isLeapYear(year):
    if year % 4 != 0:
        return 0
    if year % 100 != 0:
        return 1
    if year % 400 == 0:
        return 1
    return 0


mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def days(y, m, d):
    r = 0
    for i in range(y):
        r += 365 + isLeapYear(i)
    for i in range(0, m - 1):
        if i == 1:
            r += isLeapYear(y)
        r += mon[i]
    return r + d

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

r1 = days(y1, m1, d1)
r2 = days(y2, m2, d2)
if r2-r1 > 365243:
    print("gg")
else:
    print("D-{0}".format(r2 - r1))
