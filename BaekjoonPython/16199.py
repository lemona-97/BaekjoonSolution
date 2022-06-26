A, B, C = map(int, input().split())
D, E, F = map(int, input().split())

difY = D-A
difM = E-B
difD = F-C
year1 = 0
year2 = 0
year3 = 0
if difY > 0:
    if E > B:
        year1 = difY
    elif E == B:
        if F >= C:
            year1 = difY
        else:
            year1 = difY-1
    else:
        year1 = difY-1
else:
    year1 = 0
year2 = difY+1
year3 = difY
print(year1)
print(year2)
print(year3)