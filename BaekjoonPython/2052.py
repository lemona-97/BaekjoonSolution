N = int(input())

def exNumber(n):
    check = "%.250f" % 2 ** -n
    last = len(check)
    for i in range(last-1, 1, -1):
        if check[i] != '0':
            last = i
            break
    print(check[:last+1])

exNumber(N)