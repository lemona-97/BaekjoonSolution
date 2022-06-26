case = int(input())

for _ in range(case):
    word = input()
    count = 0
    sum = 0
    for i in range(len(word)):
        if word[i] == "O":
            count += 1
            sum += count
        else:
            count = 0
    print(sum)


