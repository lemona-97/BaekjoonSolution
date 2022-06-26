a = lambda x: True if (90 <= x <= 100) else False
b = lambda x: True if (80 <= x <= 89) else False
c = lambda x: True if (70 <= x <= 79) else False
d = lambda x: True if (60 <= x <= 69) else False
f = lambda x: True if (0 <= x < 60) else False

n = int(input())
b = list(map(lambda y:y[1] if y[0](n) else 0, ((a, 'A'), (b, 'B'), (c, 'C'), (d, 'D'), (f, 'F'))))

for i in b:
    if i:
        print(i)