N, M = map(int, input().split())
list1 = list(map(int, input().split()))
def sumNumber(n, m, listNumber):
    set1 = set()
    for i in range(1, n+1):
        for j in range(len(listNumber)):
            if i % listNumber[j] == 0:
                set1.add(i)

    sum = 0
    for i in range(len(list(set1))):
        sum += list(set1)[i]
    print(sum)
sumNumber(N, M, list1)