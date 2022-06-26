A, B, C = map(int, input().split())

if B > C:
    print("-1")
elif B == C:
    print("0")
else:
    D = (A // (C - B)) + 1
    D = int(D)
    print(D)