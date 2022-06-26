def checkLocation():
    word = input()
    alphaList = [-1 for _ in range(26)]
    for i in range(0, len(word)):
        if alphaList[ord(word[i])-97] == -1:
            alphaList[ord(word[i])-97] = i
    for j in range(len(alphaList)):
        print(alphaList[j], end=" ")
checkLocation()