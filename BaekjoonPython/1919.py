word1 = input()
word2 = input()

alphaList1 = [0 for i in range(26)]
alphaList2 = [0 for i in range(26)]

for i in range(len(word1)):
    alphaList1[ord(word1[i])-97] += 1
for i in range(len(word2)):
    alphaList2[ord(word2[i])-97] += 1

count = 0
for i in range(26):
    count += abs(alphaList1[i] - alphaList2[i])
print(count)