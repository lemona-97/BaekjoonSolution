def checkMusic():
    mList = list(map(int, input().split()))
    asCount = 0
    deCount = 0
    for i in range(len(mList)-1):
        if mList[i] < mList[i+1]:
            asCount += 1
        else:
            deCount += 1
    if asCount == 7:
        print("ascending")
    elif deCount == 7:
        print("descending")
    else:
        print("mixed")
checkMusic()