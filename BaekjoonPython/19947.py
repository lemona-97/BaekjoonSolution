H, Y = map(int, input().split())

def calculate(H, Y):
    maxMoney = [0]*(Y+1)
    maxMoney[0] = H
    for i in range(1, Y+1):
        if i - 1 >= 0 and maxMoney[i-1]:
            maxMoney[i] = max(int(maxMoney[i-1]*1.05), maxMoney[i])
        if i - 3 >= 0 and maxMoney[i-3]:
            maxMoney[i] = max(int(maxMoney[i-3]*1.2), maxMoney[i])
        if i - 5 >= 0 and maxMoney[i-5]:
            maxMoney[i] = max(int(maxMoney[i-5]*1.35), maxMoney[i])
    print(maxMoney[Y])





calculate(H, Y)