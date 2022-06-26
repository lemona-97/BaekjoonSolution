word = input()
key = input()

wordLength = len(word)
keyLength = len(key)
result = ''
for i in range(wordLength):
    if word[i] == " ":
        result += ' '
    else:
        result += chr((ord(word[i]) - ord(key[i % keyLength]) - 1) % 26 + ord('a'))
print(result)