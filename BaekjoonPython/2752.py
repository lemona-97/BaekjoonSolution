A, B, C = map(int, input().split())

max = A
mid = A
min = A

if A < B :
    if A < C :
        min = A
        if B < C:
            max = C
            mid = B
        else:
            max = B
            mid = C
    else:
        max = B
        min = C
else:
    if A > C :
        max = A
        if B < C:
            mid = C
            min = B
        else:
            min = C
            mid = B
    else:
        min = B
        max = C


print(min,mid,max)