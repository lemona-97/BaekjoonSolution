day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())
if x == 1:
    print(day[y % 7])
elif x == 2:
    print(day[(y + 31) % 7])
elif x == 3:
    print(day[(y + 31 + 28) % 7])
elif x == 4:
    print(day[(y + 31 + 28 + 31) % 7])
elif x == 5:
    print(day[(y + 31 + 28 + 31 + 30) % 7])
elif x == 6:
    print(day[(y + 31 + 28 + 31 + 30 + 31) % 7])
elif x == 7:
    print(day[(y + 31 + 28 + 31 + 30 + 31 + 30) % 7])
elif x == 8:
    print(day[(y + 31 + 28 + 31 + 30 + 31 + 30 + 31) % 7])
elif x == 9:
    print(day[(y + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31) % 7])
elif x == 10:
    print(day[(y + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30) % 7])
elif x == 11:
    print(day[(y + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31) % 7])
elif x == 12:
    print(day[(y + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30) % 7])