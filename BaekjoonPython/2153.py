def primeNumber(word):
    sum = 0
    primecheck = 0
    for i in range(len(word)):
        if ord(word[i]) < 96:
            sum += int(ord(word[i])) - 38
        else:
            sum += int(ord(word[i])) - 96
    for j in range(2, sum//2 + 1):
        if sum % j == 0:
            primecheck += 1
    if primecheck == 0:
        print("It is a prime word.")
    else:
        print("It is not a prime word.")

word1 = input()
primeNumber(word1)