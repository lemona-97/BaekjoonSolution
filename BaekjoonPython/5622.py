word = input()
totalTime = 0
for i in word:
    if i == 'A' or i == 'B' or i == 'C':
        totalTime += 3
    elif i == 'D' or i == 'E' or i == 'F':
        totalTime += 4
    elif i == 'G' or i == 'H' or i == 'I':
        totalTime += 5
    elif i == 'J' or i == 'K' or i == 'L':
        totalTime += 6
    elif i == 'M' or i == 'N' or i == 'O':
        totalTime += 7
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        totalTime += 8
    elif i == 'T' or i == 'U' or i == 'V':
        totalTime += 9
    elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        totalTime += 10
print(totalTime)