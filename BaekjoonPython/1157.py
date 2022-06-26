word = input()
wordList = [0 for _ in range(26)]

for i in word:
    if ord(i) >= 97:
        wordList[ord(i) - 97] += 1
    else:
        wordList[ord(i) - 65] += 1

count = 0
check = 0
for i in range(len(wordList)):
    if wordList[i] == max(wordList):
        count += 1
        check = i
if count == 1:
    print(chr(check + 65))
else:
    print("?")