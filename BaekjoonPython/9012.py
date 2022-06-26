T = int(input())


for _ in range(T):
    count = 0
    word = list(input())
    for j in word:
        if j == "(":
            count += 1
        elif j == ")":
            count -= 1
        if count < 0:
            print("NO")
            break
    if count == 0:
        print("YES")
    elif count > 0:
        print("NO")