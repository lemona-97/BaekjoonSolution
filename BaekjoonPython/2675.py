T = int(input())
for k in range(T):
    R, S = input().split()
    R = int(R)
    for i in S:
        for j in range(R):
            print(i, end="")
    print("")