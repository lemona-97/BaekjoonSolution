def divisionNumber(A, B):
    answer = []
    for i in range(A):
        if A % (i+1) == 0:
            answer.append(i+1)
    if len(answer) < B:
        print("0")
    else:
        print(answer[B-1])
N, K = map(int, input().split())

divisionNumber(N, K)