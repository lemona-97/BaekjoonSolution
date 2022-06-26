word = input()

difword = {}
for i in range(len(word)):
    for j in range(i+1, len(word)+1):
        difword[(word[i:j])] = ""
print(len(difword))
