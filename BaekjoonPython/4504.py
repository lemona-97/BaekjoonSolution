num = int(input())
numlist = int(input())


def findMulti(N, K):
    if K % N == 0:
        print("%s is a multiple of %s." % (K, N))
    else:
        print("%s is NOT a multiple of %s." % (K, N))


while numlist:
    findMulti(num, numlist)
    numlist = int(input())
