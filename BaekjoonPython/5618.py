n = int(input())

numList = list(map(int, input().split()))

def commonFactor(numlist):
    numlist.sort()
    if n == 2:
        for i in range(1, (numlist[0] // 2 + 1)):
            if numlist[0] % i == 0 and numlist[1] % i == 0:
                print(i)
        if numlist[1] % numlist[0] == 0:
            print(numlist[0])
    else:
        for i in range(1, (numlist[0]) // 2 + 1):
            if numlist[0] % i == 0 and numlist[1] % i == 0 and numlist[2] % i == 0:
                print(i)
        if numlist[2] % numlist[0] == 0 and numlist[1] % numlist[0] == 0:
            print(numlist[0])

commonFactor(numList)
